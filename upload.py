
"""
This script:
- edits pyproject.toml
    - finds the project version eg. 0.0.4
    - increments it by 1 eg. 0.0.5
    - if we don't do this, PyPI won't allow us to push this version
    - this is because of an "existing version conflict"
- automatically pushes your project to PyPI
- though you still need to key in your PyPI API key manually for security purposes

Note: you need to "pip install build twine" before running this
    - "build" allows us to build our PyPI project locally
    - "twine" allows us to upload our project to PyPI
"""

import os
import re

with open('pyproject.toml') as f:
    text = f.read()

old_version: str = re.findall('version = "(.*?)"', text)[0]     # "0.0.4"

major, minor, patch = old_version.split('.')            # major="0" minor="0" patch="4"

new_patch = int(patch) + 1

new_version = f'{major}.{minor}.{new_patch}'      # "0.0.5"

text = re.sub(old_version, new_version, text)

with open('pyproject.toml', 'w') as f:
    f.write(text)    

# TODO: this works for MacOS, but might not for Windows
commands = [
    'rm -rf ./dist',                    # removes current dist folder
    'python3 -m build',                 # build PyPI project
    'python3 -m twine upload dist/*'    # upload to PyPI
]

for command in commands:
    print(command)
    os.system(command)
