import pytest
from typing import Dict

example_dict = {
  "string": "Hello, World",
  "integer": 25,
  "floating_point": 3.14,
  "boolean": True,
  "null_value": None,
  "array": ["item1", "item2", "item3"],
  "object": {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
  },
  "nested": {
    "object_in_array": [
      {"key1": "value1"},
      {"key2": "value2"}
    ],
    "array_in_object": {
      "key1": ["item1", "item2"]
    }
  }
}

yaml_file_content = """
# This is a sample YAML file

# Scalars
string: "Hello, World"
integer: 25
floating_point: 3.14
boolean: true
null_value: null

# Sequences
sequence:
  - item1
  - item2
  - item3

# Mappings
mapping:
  key1: value1
  key2: value2
  key3: value3

# Nested sequences and mappings
nested:
  - key1: value1
    key2: value2
  - sequence:
      - item1
      - item2
"""

@pytest.fixture
def dummy_dict() -> Dict:
    return example_dict

@pytest.fixture
def get_example_yaml_file_content() -> str:
    return yaml_file_content

