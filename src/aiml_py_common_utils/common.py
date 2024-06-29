import os
from box.exceptions import BoxValueError
import yaml
import json
import joblib
from box import ConfigBox
from pathlib import Path
from typing import Any, List, Union, Dict
from aiml_py_common_utils.log_manager import logger

JSON_LIKE = Union[Dict[str, 'JSON_LIKE'], List['JSON_LIKE'], int, str, float, bool, None]

def simple_read_yaml(path_to_yaml: Path) -> Dict:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        Dict: dict type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.debug(f"yaml file: {path_to_yaml} loaded successfully")
            return content
    except Exception as e:
        raise e

def box_read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.debug(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


def create_directories(path_to_directories: List[Path], verbose: bool=True) -> None:
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        create_directory(path_to_directory=path, verbose=verbose)

def create_directory(path_to_directory: Path, verbose: bool=True) -> None:
    """create a single directory

    Args:
        path_to_directory (Path): path to the directory
        verbose (bool, optional): ignore debug logs if multiple dirs is to be created. Defaults to False.
    """
    os.makedirs(path_to_directory, exist_ok=True)
    if verbose:
        logger.debug(f"created directory at: {path_to_directory}")

def save_as_json(path: Path, data: JSON_LIKE, indent: int=4) -> None:
    """save json like data to json file

    Args:
        path (Path): path to json file
        data (JSON_LIKE): json like data to be saved in json file
        indent (int, optional): The number of spaces for indentation in the JSON string. If not provided, it defaults to 4.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=indent)

    logger.debug(f"json file saved at: {path}")


def simple_load_json(path: Path) -> Dict:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        Dict: json data as dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.debug(f"json file loaded succesfully from: {path}")
    return content

def box_load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.debug(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)

def save_text(data: str, path: Path) -> None:
    with open(path, "w") as f:
        f.write(data)

def stringify_json(data: Union[Dict, List[Dict]], indent: int=4) -> str:
    """
    Converts a dictionary or a list of dictionaries into a JSON string with specified indentation.

    Args:
        data (Union[Dict, List[Dict]]): The dictionary or list of dictionaries that needs to be converted into a JSON string.
        indent (int, optional): The number of spaces for indentation in the JSON string. If not provided, it defaults to 4.

    Returns:
        str: The input data formatted as a JSON string with the specified indentation.
    """
    return json.dumps(obj=data, indent=indent)


def save_bin(data: Any, path: Path) -> None:
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.debug(f"binary file saved at: {path}")


def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.debug(f"binary file loaded from: {path}")
    return data

def get_size(path: Path) -> float:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        float: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    logger.debug(f"size of: {path} =~ {size_in_kb} KB")
    return size_in_kb

def word_wrap(string: str, n_chars: int=72) -> str:
    """Breaks a string into lines at the next space beyond n_chars.

    Parameters:
        string (str): The string that needs to be printed.
        n_chars (int, optional): The string is broken into lines after n_chars. Defaults to 72.

    Returns:
        str: The input string formatted with line breaks.
    """
    if len(string) < n_chars:
        return string
    else:
        return \
            string[:n_chars].rsplit(' ', 1)[0] \
            + '\n' \
            + word_wrap(string[len(string[:n_chars].rsplit(' ', 1)[0])+1:], n_chars)
