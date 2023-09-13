import logging
from typing import Any
import pandas as pd
import yaml
import json
import gcsfs

# from .log_utils import logger


def read_data(path: str) -> Any:
    if path.endswith(".json"):
        if path.startswith("gs://"):
            fs = gcsfs.GCSFileSystem(project="dst-dev2021")
            with fs.open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        else:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
    elif path.endswith(".txt"):
        with open(path, "r", encoding="utf-8") as f:
            data = f.read()
        data = data.split("\n")
    elif path.endswith(".csv"):
        data = pd.read_csv(path)
    elif path.endswith(".ndjson"):
        data = pd.read_json(path, lines=True, orient="records")
    elif path.endswith(".ndjson.gz"):
        data = pd.read_json(path, lines=True, orient="records", compression="gzip")
    elif path.endswith(".pickle"):
        data = pd.read_pickle(path)
    elif path.endswith(".parquet"):
        data = pd.read_parquet(path)
    elif path.endswith(".yaml"):
        with open(path, "r") as stream:
            try:
                data = yaml.safe_load(stream)
            except yaml.YAMLError as e:
                logging.error(e)
    else:
        data = []
    return data


def save_data(data: Any, path: str, append: bool) -> None:
    if path.endswith(".json"):
        if path.startswith("gs://"):
            fs = gcsfs.GCSFileSystem(project="dst-dev2021")
            with fs.open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        else:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
    elif path.endswith(".txt") and isinstance(data, list):
        if append:
            with open(path, "a", encoding="utf-8") as f:
                for _d in data:
                    f.write(_d)
                    f.write("\n")
        else:
            with open(path, "w", encoding="utf-8") as f:
                for _d in data:
                    f.write(_d)
                    f.write("\n")
    elif path.endswith(".csv"):
        data.to_csv(path, index=False)
    elif path.endswith(".ndjson"):
        data.to_json(path, lines=True, orient="records")
    elif path.endswith(".ndjson.gz"):
        data.to_json(path, lines=True, orient="records", compression="gzip")
    elif path.endswith(".pickle"):
        data.to_pickle(path)
    elif path.endswith(".parquet"):
        data.to_parquet(path)
    elif isinstance(data, list):
        if append:
            with open(path, "a", encoding="utf-8") as f:
                for _d in data:
                    f.write(_d)
                    f.write("\n")
        else:
            with open(path, "w", encoding="utf-8") as f:
                for _d in data:
                    f.write(_d)
                    f.write("\n")
    else:
        pass


def cut_list_in_to_string_lists(string_items: list, max_len: int):

    i = j = 0
    cutted_lists = []
    while j < len(string_items):
        if len(",".join(string_items[i : j + 1])) > max_len:
            cutted_lists.append(string_items[i:j])
            i = j

        j += 1

    return cutted_lists if cutted_lists else [string_items]
