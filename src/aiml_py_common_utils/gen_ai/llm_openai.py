import tiktoken
from tiktoken import Encoding

# Load the GPT-3.5-turbo model
enc_gpt35_turbo = tiktoken.encoding_for_model("gpt-3.5-turbo")

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