"""
Reference - https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb
--------------------------------------------------------------------------
Encoding name          | OpenAI models
-----------------------|--------------------------------------------------
cl100k_base            | gpt-4, gpt-3.5-turbo, text-embedding-ada-002, 
                       | text-embedding-3-small, text-embedding-3-large
p50k_base              | Codex models, text-davinci-002, text-davinci-003
r50k_base (or gpt2)    | GPT-3 models like davinci
"""

import tiktoken
from tiktoken import Encoding

# Load the GPT-3.5-turbo model
enc_gpt35_turbo = tiktoken.encoding_for_model("gpt-3.5-turbo")

# encoding for gpt-4, gpt-3.5-turbo, text-embedding-ada-002, text-embedding-3-small, text-embedding-3-large
encoding = tiktoken.get_encoding("cl100k_base")

def _num_of_tokens(string: str, enc: Encoding) -> int:
    """calculate number of tokens from input string as per the LLM model encoding

    Args:
        string (str): string input for calculating number of tokens
        enc (Encoding): encoding to used for encoding strings as per the LLM model

    Returns:
        int: number of tokens in string passed as argument
    """
    num_tokens = len(enc.encode(string))
    return num_tokens

def num_of_tokens_gpt35_turbo(string: str, enc: Encoding=enc_gpt35_turbo) -> int:
    """calculate number of tokens from input string as per the GPT3.5-Turbo model encoding

    Args:
        string (str): string input for calculating number of tokens
        enc (Encoding): encoding to used for encoding strings as per the GPT3.5-Turbo model

    Returns:
        int: number of tokens in string passed as argument
    """
    return _num_of_tokens(string=string, enc=enc)

def num_of_tokens_gpt4(string: str, enc: Encoding=encoding) -> int:
    """calculate number of tokens from input string as per the gpt-4 model encoding

    Args:
        string (str): string input for calculating number of tokens
        enc (Encoding): encoding to used for encoding strings as per the gpt-4 model

    Returns:
        int: number of tokens in string passed as argument
    """
    return _num_of_tokens(string=string, enc=enc)

def num_of_tokens_embedding_models(string: str, enc: Encoding=encoding) -> int:
    """Calculate the number of tokens in the input string for the 
        text-embedding-ada-002, 
        text-embedding-3-small, and 
        text-embedding-3-large embedding models.

    Args:
        string (str): string input for calculating number of tokens
        enc (Encoding):The encoding to be used as per the 3 models

    Returns:
        int: number of tokens in string passed as argument
    """
    return _num_of_tokens(string=string, enc=enc)