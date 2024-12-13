import sys

from .helper import print_qn_n_options

from unprint import unprint
from onkeypress import while_not_exit, onkeypress, Key

def select(
    question: str,
    options: list[str],
    pointer: str = "=>",
    color: str = "green",
    background_color: str = "",
) -> str:
    """
    Creates select interface in temrinal

    Eg.
        Select favourite fruit (Up/Down to navigate, Enter to confirm):
        => apple
        orange
        pear

    Args:
        question (str): question to be asked
        options (list[str]): list of available options

        pointer (str): printed in front of selected option
        color (str): selected option's color eg. "red", "green", "blue"
        background_color (str): selected option's background color

    Returns:
        (str): user-selected option
    """
    qn_kwargs = {  # common kwargs to pass into print_qn_n_options()
        "question": question,
        "options": options,
        "pointer": pointer,
        "color": color,
        "background_color": background_color,
    }

    def on_arrow_keypress(
        key_str: str,
        state: dict,
    ) -> None:
        """
        Callback called when Up or Down arrow key is pressed
        """
        diff: int = -1 if key_str == "up" else 1
        new_option_index_to_focus: int = state["option_index_to_focus"] + diff

        if new_option_index_to_focus < 0 or new_option_index_to_focus >= len(options):
            return  # out of bounds
        
        unprint(state["num_chars_printed"])

        state["option_index_to_focus"] = new_option_index_to_focus

        num_chars_printed: int = print_qn_n_options(
            **qn_kwargs,
            option_index_to_focus=state["option_index_to_focus"]
        )

        state["num_chars_printed"] = num_chars_printed

    num_chars_printed = print_qn_n_options(**qn_kwargs)

    state: dict = {
        "option_index_to_focus": 0,
        "num_chars_printed": num_chars_printed
    }

    while_not_exit(
        onkeypress(Key.UP).call(on_arrow_keypress).args("up", state),
        onkeypress(Key.DOWN).call(on_arrow_keypress).args("down", state),
        exit_key=Key.ENTER,
    )

    selected_index: int = state["option_index_to_focus"]
    return options[selected_index]


__all__ = ["select"]