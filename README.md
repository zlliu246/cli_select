
# cli_select

A package that allows MCQ select in terminal/CLI

# Installation

```
pip install cli_select
```

# Quickstart

use Up and Down arrow keys to select your option
use Enter key to confirm your selection


```python
from cli_select import select

selected = select(
    "Which is your favourite fruit?", 
    ["apple", "orange", "pear", "pineaple", "durian"],
    color="green",
)

print(f"you selected {selected}")

# Select favourite fruit (Up/Down to navigate, Enter to select):

# => apple
# orange
# pear
# pineaple
# durian
```

