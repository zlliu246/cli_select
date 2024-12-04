from src.cli_select import select

selected = select(
    "Select favourite fruit (Up/Down to navigate, Enter to select):", 
    ["apple", "orange", "pear", "pineaple", "durian"],
    color="green",
)

print(f"you selected {selected}")

