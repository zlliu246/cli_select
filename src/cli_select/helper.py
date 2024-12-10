from colorama import Fore, Back, Style

def print_qn_n_options(
    question: str,
    options: list[str],
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
    RESET_STYLE: str = Fore.RESET + Back.RESET + Style.RESET_ALL

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
