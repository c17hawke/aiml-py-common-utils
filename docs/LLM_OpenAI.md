# LLM OpenAI Common Utilities

This utility contains the following utilities - 

1. **Token calculator for GPT3.5-Turbo model**: It can calculate the number of tokens as per the GPT3.5-Turbo model.

Examples - 

```python
from aiml_py_common_utils.gen_ai import num_of_tokens_gpt35_turbo

sentence = "Hi there, how are you?"

tokens = num_of_tokens_gpt35_turbo(string=sentence)
print(tokens) # outputs = 7
```