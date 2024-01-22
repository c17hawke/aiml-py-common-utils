import pytest
from tiktoken import Encoding

# Assuming your functions are in a module named 'my_module'
from aiml_py_common_utils.gen_ai import num_of_tokens_gpt35_turbo
from aiml_py_common_utils.gen_ai.llm_openai import enc_gpt35_turbo

def test_num_of_tokens_gpt35_turbo_mocker(mocker):
    # Mock the Encoding object and its encode method
    mock_encoding = mocker.MagicMock(spec=Encoding)
    mock_encoding.encode.return_value = [2028, 374, 264, 1296, 925, 13]  # Adjust this return value based on your needs

    test_string = "This is a test string."

    # Call the function with the mocked encoding
    result = num_of_tokens_gpt35_turbo(test_string, mock_encoding)

    # Assert that the encode method was called with the correct argument
    mock_encoding.encode.assert_called_once_with(test_string)

    # Assert that the function returned the correct result
    assert result == 6  # This should match the length of the list returned by the mocked encode method

def test_num_of_tokens_gpt35_turbo():
    # Mock the Encoding object and its encode method
    test_string = "This is a test string."

    # Call the function with the mocked encoding
    result = num_of_tokens_gpt35_turbo(test_string, enc=enc_gpt35_turbo)

    # Assert that the function returned the correct result
    assert result == 6  # This should match the length of the list returned by the mocked encode method
