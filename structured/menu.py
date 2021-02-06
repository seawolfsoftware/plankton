#!/usr/bin/env python3

from simple_term_menu import TerminalMenu


def main():
    options = ['[c] Create order', '[s] View Account Summary', '[d] View Account Details', '[e] Exit']
    submenu_options = ['[e] Exit']

    terminal_menu = TerminalMenu(options,
                                 title="\n ~ plankton ~\n",
                                 menu_highlight_style=("underline", "fg_cyan"),
                                 menu_cursor=" --->  ",
                                 accept_keys=("enter", "alt-d", "ctrl-i", "c", "d", "s"),
                                 menu_cursor_style=("fg_cyan", "bold"),
                                 # exit_on_shortcut=False,
                                 clear_menu_on_exit=True)

    submenu = TerminalMenu(submenu_options,
                                 title="\n ~ Creating an Order ~\n",
                                 menu_highlight_style=("underline", "fg_cyan"),
                                 menu_cursor=" --->  ",
                                 accept_keys=("enter", "alt-d", "ctrl-i", "c", "d", "s"),
                                 menu_cursor_style=("fg_cyan", "bold"),
                                 # exit_on_shortcut=False,
                                 clear_menu_on_exit=True)

    exiting = False

    while not exiting:

        option_index = terminal_menu.show()
        option_choice = options[option_index]

        if option_choice == "[c] Create order":
            print(option_choice)
            submenu.show()

        elif option_choice == "[s] View Account Summary":
            print(option_choice)

        elif option_choice == "[d] View Account Details":
            print(option_choice)

        elif option_choice == "[e] Exit":
            print(option_choice)
            exiting = True


if __name__ == "__main__":
    main()
