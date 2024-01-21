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

