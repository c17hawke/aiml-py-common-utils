from aiml_py_common_utils import (
    save_as_json,
    simple_read_yaml,
    box_read_yaml,
    create_directories,
    simple_load_json,
    box_load_json,
    stringify_json,
    get_size
)
import json
from _pytest.fixtures import FixtureFunction
from pathlib import Path
import pytest
from box import ConfigBox
import os
from aiml_py_common_utils import logger

def test_save_as_json(mocker: FixtureFunction) -> None:
    # Mocking the open function, json.dump and logger.debug
    mocker.patch("builtins.open", mocker.mock_open())
    mocker.patch("json.dump")

    test_path = Path("test.json")
    test_data = {"key": "value"}

    save_as_json(test_path, test_data)

    # Assert that json.dump was called with the correct arguments
    json.dump.assert_called_once_with(test_data, mocker.ANY, indent=4)


def test_simple_read_yaml_success(mocker: FixtureFunction) -> None:
    # Mocking the yaml.safe_load and open functions
    mocker.patch("yaml.safe_load", return_value={"key": "value"})
    mocker.patch("builtins.open", mocker.mock_open())

    path_to_yaml = Path("test.yaml")
    result = simple_read_yaml(path_to_yaml)

    assert result == {"key": "value"}


def test_simple_read_yaml_failure(mocker: FixtureFunction) -> None:
    # Mocking the yaml.safe_load to raise an exception
    mocker.patch("yaml.safe_load", side_effect=Exception("Test Exception"))
    mocker.patch("builtins.open", mocker.mock_open())

    path_to_yaml = Path("test.yaml")

    with pytest.raises(Exception) as e:
        simple_read_yaml(path_to_yaml)

    assert str(e.value) == "Test Exception"


def test_box_read_yaml_success(mocker: FixtureFunction) -> None:
    # Mocking the yaml.safe_load and open functions
    mocker.patch("yaml.safe_load", return_value={"key": "value"})
    mocker.patch("builtins.open", mocker.mock_open())

    path_to_yaml = Path("test.yaml")
    result = box_read_yaml(path_to_yaml)

    assert result == ConfigBox({"key": "value"})
    assert isinstance(result, ConfigBox)


def test_box_read_yaml_failure(mocker: FixtureFunction) -> None:
    # Mocking the yaml.safe_load to raise an exception
    mocker.patch("yaml.safe_load", side_effect=Exception("Test Exception"))
    mocker.patch("builtins.open", mocker.mock_open())

    path_to_yaml = Path("test.yaml")

    with pytest.raises(Exception) as e:
        box_read_yaml(path_to_yaml)

    assert str(e.value) == "Test Exception"


def test_create_directories_success(mocker: FixtureFunction) -> None:
    # Mocking the os.makedirs and logger.debug functions
    mocker.patch("os.makedirs")
    mocker.patch("loguru.logger.debug")

    path_to_directories = [Path("path/to/dir1"), Path("path/to/dir2")]
    create_directories(path_to_directories)

    # Assert that os.makedirs was called for each directory
    assert os.makedirs.call_count == len(path_to_directories)


def test_simple_load_json_success(mocker: FixtureFunction) -> None:
    # Mocking the yaml.safe_load and open functions
    mocker.patch("json.load", return_value={"key": "value"})
    mocker.patch("builtins.open", mocker.mock_open())

    path = Path("path/to/json")
    result = simple_load_json(path)

    assert result == {"key": "value"}


def test_box_load_json_success(mocker: FixtureFunction) -> None:
    # Mocking the yaml.safe_load and open functions
    mocker.patch("json.load", return_value={"key": "value"})
    mocker.patch("builtins.open", mocker.mock_open())

    path = Path("path/to/json")
    result = box_load_json(path)

    assert result == ConfigBox({"key": "value"})
    assert isinstance(result, ConfigBox)


def test_stringify_json_dict() -> None:
    data = {"key": "value"}
    result = stringify_json(data)
    expected_result = '{\n    "key": "value"\n}'

    assert result == expected_result


def test_stringify_json_list_of_dicts() -> None:
    data = [{"key1": "value1"}, {"key2": "value2"}]
    result = stringify_json(data)
    expected_result = '[\n    {\n        "key1": "value1"\n    },\n    {\n        "key2": "value2"\n    }\n]'

    assert result == expected_result


def test_stringify_json_indent() -> None:
    data = {"key": "value"}
    result = stringify_json(data, indent=2)
    expected_result = '{\n  "key": "value"\n}'

    assert result == expected_result


def test_get_size_success(mocker: FixtureFunction) -> None:
    # Mocking the os.path.getsize function
    mocker.patch('os.path.getsize', return_value=2048)

    path = Path('path/to/file')
    result = get_size(path)

    # Assert that os.path.getsize was called with the correct argument
    os.path.getsize.assert_called_once_with(path)

    # Assert that the result is as expected
    assert result == 2  # 2048 bytes is 2 KB
