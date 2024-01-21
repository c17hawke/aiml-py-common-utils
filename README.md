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

print(content.string) # prints "Hello, World"
print(content.integer) # prints 25

# And similarly other content as well
```

### 2. Create multiple directories

Let's say you have to create multiple directories like - `dir_one`, `dir_two` and `dir_three`. So you can use this function as follows - 

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

### 4. load a JSON file

For a sample JSON file at the given path containing- 

```JSON
{
  "string": "Hello, World",
  "integer": 25,
  "floating_point": 3.14,
  "boolean": true,
  "null_value": null,
}
```

The python code will look like - 

```python
from pathlib import Path
from aiml_py_common_utils import load_json

path = Path("path/to/example.json")
content = load_json(path=path_to_json)
print(content.string) # prints "Hello, World"
print(content.integer) # prints 25
```

### 5. Save a binary file 

You can save a snapshot of a data using this function

```python
from pathlib import Path
from aiml_py_common_utils import save_bin

example_dict = example_dict = {
  "string": "Hello, World",
  "integer": 25,
  "floating_point": 3.14,
  "boolean": True,
  "null_value": None,
}
path_to_bin = Path("path/to/example.bin")
save_bin(data=example_dict, path=path_to_bin)
```

### 6. Load a binary file 

You can Load the snapshot of a data saved above using this function later on

```python
from pathlib import Path
from aiml_py_common_utils import load_bin

path_to_bin = Path("path/to/example.bin")

loaded_bin_content = load_bin(path=path_to_bin)
```

### 7. Get size of a file in KBs

To get the size of a file in `KiloBytes` you can use the following function

```python
from pathlib import Path
from aiml_py_common_utils import get_size

filepath = Path("path/to/example.file")

size_in_kb = get_size(path=filepath)
```