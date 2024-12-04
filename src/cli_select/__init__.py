import sys
from toggle_cbreak import cbreak_off, cbreak_on
from unprint import unprint
from colorama import Fore, Back, Style

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

    ESCAPE_CHARACTER_TO_NAME_MAP: dict[str, str] = {
        '\x1b[A': "Up",
        '\x1b[B': "Down",
    }

    def print_qn_n_options(
        option_index_to_focus: int = 0,
        pointer: str = "=>",
        color: str = "",
        background_color: str = "",
    ) -> int:
        """
        Prints question and options for users to see
        Highlights option where index == option_index_to_focus

        Args:
            option_index_to_focus (int): index where option is selected
            pointer, color, background_color: inherited from parent function
        
        Returns:
            (int): number of lines printed by this function
        """
        RESET_STYLE = Fore.RESET + Back.RESET + Style.RESET_ALL

        def get_colorama_color(
            color_name: str,        # eg. "red", "green", "yellow"
            kind: str = "fore"      #  eg. "fore", "back"
        ) -> str: # eg. Fore.RED, Fore.GREEN, Fore.YELLOW
            try:
                return getattr(
                    Fore if kind=="fore" else Back if kind=="back" else None, 
                    color_name.upper()
                )
            except:
                return ""

        print(RESET_STYLE)
        print(RESET_STYLE + question)
        print(RESET_STYLE)

        for index, option in enumerate(options):
            option = option.replace("\n", "")  # options shouldn't have newlines inside
            if index == option_index_to_focus:
                style = (
                    get_colorama_color(color, kind="fore") +
                    get_colorama_color(background_color, kind="back") +
                    pointer
                )
                print(style, option)
            else:
                print(RESET_STYLE + option)

        print(RESET_STYLE, end="")
        return len(options) + 3 + question.count("\n")

    try:
        cbreak_on()

        num_chars_printed = print_qn_n_options(
            pointer=pointer,
            color=color,
            background_color = background_color,
        )

        current_option_index: int = 0
        last3chars: str = "---"

        while True:
            input_char = sys.stdin.read(1)

            if input_char == "\n":  # return when user hits Enter
                return options[current_option_index]
        
            last3chars = last3chars[1:] + input_char

            # handle only when user keys in Up or Down
            if last3chars not in ESCAPE_CHARACTER_TO_NAME_MAP:
                continue

            key_name: str = ESCAPE_CHARACTER_TO_NAME_MAP[last3chars]

            if key_name == "Up":
                if current_option_index <= 0: 
                    # prevent index from going below 0
                    continue
                current_option_index -= 1

            elif key_name == "Down":
                if current_option_index >= len(options) - 1:
                    # prevent index from going out of bounds
                    continue
                current_option_index += 1
            
            unprint(num_chars_printed)

            num_chars_printed: int = print_qn_n_options(
                option_index_to_focus=current_option_index,
                pointer=pointer,
                color=color,
                background_color = background_color,
            )

    finally:
        # always set terminal back to cooked mode
        print()
        cbreak_off()

__all__ = ["select"]