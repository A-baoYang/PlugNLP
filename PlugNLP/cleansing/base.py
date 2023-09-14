import arrow
import ast
import json
import pandas as pd
import sys
import os
from pathlib import Path
from tqdm import tqdm

root_dir = Path(__file__).absolute().parents[1]

sys.path.append(str(root_dir))
from utils.openai_utils import OpenAIWrapper
from utils.data_utils import cut_list_in_to_string_lists, read_data, save_data
from utils.log_utils import logger


class TextCleanser:

    def __init__(self, api_token: str = None, credential_file: str = None) -> None:
        self.task_type = "cleansing"
        self.model_api = OpenAIWrapper(
            api_token=api_token, credential_file=credential_file
        )
        self.model_name = "gpt-3.5-turbo"
        self.max_tokens = 2048
        self.default_dictionary = read_data(f"{root_dir}/dictionary/default.json")

    def set_dictionary(self, import_dictionary=None, import_filepath=None):
        if import_dictionary is not None and isinstance(import_dictionary, dict):
            self.default_dictionary = import_dictionary
        elif import_filepath is not None and isinstance(import_filepath, str):
            self.default_dictionary = read_data(import_filepath)
        else:
            pass

    def set_prompt(
        self, role: str, prompt_template: str, inputs: list, **kwargs
    ) -> None:
        """
        kwargs: 設定 prompt_template 除 inputs 之外的參數
        """

        assert "{inputs}" in prompt_template, Exception(
            "Should set inputs param in prompt_template"
        )

        self.role = role
        self.messages = []
        prompt_tpl_len = len(prompt_template)
        input_max_len = self.max_tokens - prompt_tpl_len

        self.inputs = [
            item for item in list(set(inputs)) if item not in self.default_dictionary
        ]

        cutted_lists = cut_list_in_to_string_lists(
            string_items=self.inputs, max_len=input_max_len
        )
        for cl in cutted_lists:
            prompt = prompt_template.format(inputs=cl, **kwargs)
            message = [{"role": role, "content": prompt}]
            self.messages.append(message)

        logger.info(
            f"Role: {self.role}\nComposed message: {self.messages[0]}\n#message: {len(self.messages)}"
        )

    def run(self, run_name: str, temp_output_dir: str, **kwargs):
        """
        kwargs: 設定 OpenAI API 參數
        """
        os.makedirs(temp_output_dir, exist_ok=True)
        current_datetime = arrow.now(tz="Asia/Taipei").format("YYYYMMDDTHHmmss")
        self.task_name = f"{self.task_type}-{run_name}-{current_datetime}"
        self.result = []
        self.failed_messages = []
        for i, msg in enumerate(self.messages):
            try:
                _res = self.model_api.get_chat_completion(messages=msg, **kwargs)
                # 僅處理 json 格式 output
                _dict = ast.literal_eval(_res)
                self.result.append(_dict)
                self.rearrange_dictionaries(_dict)
            except:
                self.failed_messages.append(msg)

            if i > 10 and i % 10 == 0:
                save_data(
                    path=f"{temp_output_dir}/task_result-{self.task_name}.parquet",
                    data=pd.DataFrame({"result": self.result}),
                    append=False,
                )

        save_data(
            path=f"{temp_output_dir}/task_result-{self.task_name}.parquet",
            data=pd.DataFrame({"result": self.result}),
            append=False,
        )
        save_data(
            path=f"{temp_output_dir}/failed_messages-{self.task_name}.parquet",
            data=pd.DataFrame({"messages": self.failed_messages}),
            append=False,
        )

        return self.result

    def update_dictionary(self, new_dict: dict):
        assert isinstance(new_dict, dict), raise Exception("Need to be dictionary to update")

        self.default_dictionary.update(new_dict)

        save_data(data=self.default_dictionary, path=f"{root_dir}/dictionary/default.json")
