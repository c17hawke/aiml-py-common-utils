from aiml_py_common_utils import save_dict2json
import json
import pytest # noqa
from pathlib import Path

def test_save_dict2json(mocker):
    # Mocking the open function, json.dump and logger.debug
    mocker.patch('builtins.open', mocker.mock_open())
    mocker.patch('json.dump')

    test_path = Path('test.json')
    test_data = {"key": "value"}

    save_dict2json(test_path, test_data)

    # Assert that json.dump was called with the correct arguments
    json.dump.assert_called_once_with(test_data, mocker.ANY, indent=4)

