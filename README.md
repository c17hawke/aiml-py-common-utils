# AIML PYTHON COMMON UTILS

This repository contains the most commonly used utilities that can be used in almost any AIML application.

## Current Version contains the following utilities - 

### 1. Read YAML file and return the ConfigBox type object -

for a yaml file like this - 

```yaml
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
```
You can access the content of yaml as follows- 

```python
from aiml_py_common_utils import read_yaml

content = read_yaml(path_to_yaml)

print(content.string)
print(content.integer)

# And similarly other content as well
```

### 2. Create multiple directories

Let's say you have to create multiple directories like - "dir_one", "dir_two" and "dir_three". So you can use this function as follows - 

```python
from pathlib import Path
from aiml_py_common_utils import create_directories

list_of_directories_paths = [
    Path("./dir_one"),
    Path("./dir_two"),
    Path("./dir_three")
]

create_directories(path_to_directories= list_of_directories_paths)
```

### 3. Save the directory as a JSON file


```python
from pathlib import Path
from aiml_py_common_utils import save_dict2json

example_dict = example_dict = {
  "string": "Hello, World",
  "integer": 25,
  "floating_point": 3.14,
  "boolean": True,
  "null_value": None,
}
path_to_json = Path("path/to/example.json")
save_dict2json(path=path_to_json)
```