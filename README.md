# AIML Python Common Utilities

> **Visit Documentation - [Click here](https://c17hawke.github.io/aiml-py-common-utils/)**

This repository provides a collection of utilities that are frequently used in various AIML applications.

## Current Version Features

The current version includes the following utilities:

### 1. Simple YAML File Reader

This utility reads a YAML file and returns a dictionary type object. For instance, given a YAML file with the following content:

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

You can access the content of the YAML file as follows:

```python
import aiml_py_common_utils as aiml

content = aiml.simple_read_yaml(path_to_yaml)

print(content["string"])  # Outputs: "Hello, World"
print(content["integer"])  # Outputs: 25
```

### 2. Box YAML File Reader

This utility reads a YAML file and returns a ConfigBox type object. For instance, given a YAML file with the following content:

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

You can access the content of the YAML file as follows:

```python
import aiml_py_common_utils as aiml

content = aiml.box_read_yaml(path_to_yaml)

print(content.string)  # Outputs: "Hello, World"
print(content.integer)  # Outputs: 25
```

### 3. Directory Creator

This utility allows you to create multiple directories. For example, to create directories named `dir_one`, `dir_two`, and `dir_three`, you can use the function as follows:

```python
from pathlib import Path
import aiml_py_common_utils as aiml

list_of_directories_paths = [
    Path("./dir_one"),
    Path("./dir_two"),
    Path("./dir_three")
]

aiml.create_directories(path_to_directories=list_of_directories_paths)
```

### 4. JSON File Writer

This utility saves a dict or list as a JSON file:

```python
from pathlib import Path
import aiml_py_common_utils as aiml

example_dict = {
  "string": "Hello, World",
  "integer": 25,
  "floating_point": 3.14,
  "boolean": True,
  "null_value": None,
}

path_to_json = Path("path/to/example.json")
aiml.save_as_json(path=path_to_json)
```

### 5. Simple JSON File Reader

This utility loads a JSON file as dictionary/list. For example, given a JSON file at a certain path containing:

```JSON
{
  "string": "Hello, World",
  "integer": 25,
  "floating_point": 3.14,
  "boolean": true,
  "null_value": null,
}
```

You can load the content of the JSON file as follows:

```python
from pathlib import Path
import aiml_py_common_utils as aiml

path = Path("path/to/example.json")
content = load_json(path=path_to_json)
print(content["string"])  # Outputs: "Hello, World"
print(content["integer"])  # Outputs: 25
```

### 6. Binary File Writer

This utility saves a snapshot of data as a binary file:

```python
from pathlib import Path
import aiml_py_common_utils as aiml

example_dict = {
  "string": "Hello, World",
  "integer": 25,
  "floating_point": 3.14,
  "boolean": True,
  "null_value": None,
}

path_to_bin = Path("path/to/example.bin")
aiml.save_bin(data=example_dict, path=path_to_bin)
```

### 7. Binary File Reader

This utility loads a snapshot of data from a binary file:

```python
from pathlib import Path
import aiml_py_common_utils as aiml

path_to_bin = Path("path/to/example.bin")
loaded_bin_content = aiml.load_bin(path=path_to_bin)
```

### 8. File Size Calculator

This utility calculates the size of a file in kilobytes:

```python
from pathlib import Path
import aiml_py_common_utils as aiml

filepath = Path("path/to/example.file")
size_in_kb = aiml.get_size(path=filepath)
```

### 9. Convert dict/json as string

This utility converts a dictionary or a list of dictionaries into a JSON string with specified indentation.

```python
from pathlib import Path
from aiml_py_common_utils import stringify_json

json_as_string = stringify_json(data={"key": "value"})
```
