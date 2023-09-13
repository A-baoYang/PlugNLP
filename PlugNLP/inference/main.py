import json
from typing import Union

from langdetect import detect

from ..openai_func import OpenAIWrapper
from ..utils import LANGUAGES
from .config import task_config


class PlugNLP:
    def __init__(
        self,
        api_token: Union[str, None] = None,
        credential_file: Union[str, None] = "~/secret.cfg",
    ):
        self.model_api = OpenAIWrapper(api_token, credential_file)

    def compose_prompt(
        self,
        task_type: str,
        example_list: Union[list, None] = None,
        detected_lang: str = "en",
    ):
        """generate prompt according to different task type"""
        prompt = f'you are now a {task_config["task_role"][task_type]}.\n'
        if example_list is not None:
            prompt += "According to the example data, \n"
        prompt += (
            f'{task_config["action_msg"][task_type]}, no need to explain reason, '
            f'just reply the {task_config["result_type"][task_type]}'
        )
        if task_type not in ["classify", "generate"]:
            prompt += f" in {LANGUAGES[detected_lang]}"
        if task_type in ["classify", "extract"]:
            prompt += (
                "\nTotal answer number must be the same as length of new data.\n\n"
            )
        else:
            prompt += "\n\n"
        if example_list is not None:
            prompt += (
                f"Example data: \n{json.dumps(example_list, ensure_ascii=False)}\n\n"
            )
        if task_type == "classify" and example_list is not None:
            prompt += (
                "Label classes: "
                f'{", ".join(list(set([item["label"] for item in example_list])))}\n\n'
            )
        return prompt

    def basis_func(
        self,
        task_type: str,
        text_list: Union[list, None],
        example_list: Union[list, None] = None,
        **kwargs,
    ):
        detected_lang = detect(", ".join([item["text"] for item in text_list]))
        prompt = (
            self.compose_prompt(
                task_type=task_type,
                example_list=example_list,
                detected_lang=detected_lang,
            )
            + f"New data:\n{json.dumps(text_list, ensure_ascii=False)}\n\n"
        )
        messages = [{"role": "user", "content": prompt}]
        results = self.model_api.get_chat_completion(messages=messages, **kwargs)
        # try:
        #     assert len(results.split(",")) == len(example_list)
        # except Exception:
        #     raise Exception(
        #         "Number of reply is not equal to text_list you just provided"
        #     )
        return results

    def classify(
        self,
        text_list: Union[list, None],
        example_list: Union[list, None] = None,
        **kwargs,
    ):
        return self.basis_func(
            task_type="classify",
            text_list=text_list,
            example_list=example_list,
            generation_params={"temperature": 0.1},
            **kwargs,
        )

    def extract(
        self,
        text_list: Union[list, None],
        example_list: Union[list, None] = None,
        **kwargs,
    ):
        return self.basis_func(
            task_type="extract",
            text_list=text_list,
            example_list=example_list,
            generation_params={"temperature": 0.1},
            **kwargs,
        )

    def qa(
        self,
        text_list: Union[list, None],
        example_list: Union[list, None] = None,
        **kwargs,
    ):
        return self.basis_func(
            task_type="qa",
            text_list=text_list,
            example_list=example_list,
            **kwargs,
        )

    def summarize(
        self,
        text_list: Union[list, None],
        example_list: Union[list, None] = None,
        **kwargs,
    ):
        return self.basis_func(
            task_type="summarize",
            text_list=text_list,
            example_list=example_list,
            **kwargs,
        )

    def generate(
        self,
        text_list: Union[list, None],
        example_list: Union[list, None] = None,
        **kwargs,
    ):
        return self.basis_func(
            task_type="generate",
            text_list=text_list,
            example_list=example_list,
            **kwargs,
        )
