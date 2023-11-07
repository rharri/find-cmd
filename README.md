## Description
A Python implementation of the `find` command line program. This implementation
is partial and only supports the `-name` and `-print` options.

## Requirements
- Python >=3.12

## Example
```
$ python3 -m find_cmd . -name "*.py" -print
find_cmd/__init__.py
find_cmd/cli.py
find_cmd/__main__.py
find_cmd/tests/__init__.py
.venv/lib/python3.12/site-packages/pip/__init__.py
.venv/lib/python3.12/site-packages/pip/__pip-runner__.py
.venv/lib/python3.12/site-packages/pip/__main__.py
...
...
...
```
