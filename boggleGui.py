# ##########################
# FILE:boggleGui.py
# WRITER:Ofer Ezrachi,oferezr, 209350586
# WRITER:Bar Cavia, barcavia123, 316032622
# EXERCISE: intro2cs1 ex12 2021
# DESCRIPTION: GUI for the boggle model
# ##########################

import tkinter as tk
from bogglemodel import *

TIME_LEFT = "Time left: "
SUBMIT = "Submit"
HELLO_MSG = "Welcome to the boggel game!"
START_GAME = "Click the button to start"
END_TIME_MSG = "You run out of time..."
PLAY_AGAIN = "Play again?"
CURRENT_WORD = "Current word:"
FOUND_WORDS = "Found words:\n"
SCORE = "Score: "

BUTTON_HOVER_COLOR = 'gray'
REGULAR_COLOR = '#c8c9c3'
BUTTON_ACTIVE_COLOR = '#0096c4'

LETTER_BUTTON_STYLE = {"font": ("Courier", 25, "bold"),
                       "borderwidth": 3,
                       "relief": tk.RAISED,
                       "bg": REGULAR_COLOR,
                       "fg": "#005b77",
                       "width": 5,
                       "height":2,
                       "bd": 6,
                       "activebackground": BUTTON_ACTIVE_COLOR}

SUBMIT_BUTTON_STYLE = {"font": ("Courier", 16, "bold"),
                       "borderwidth": 1,
                       "relief": tk.RAISED,
                       "bg": REGULAR_COLOR,
                       "fg": "#005b77",
                       "width": 8,
                       "bd": 4,
                       "activebackground": "#96c400"}
STARTING_LABEL_STYLE = {"font": ("Courier", 23, "bold"),
                        "bg": "#0096c4",
                        "fg": "#ffffff",
                        "height": 2}
SUB_STARTING_LABEL_STYLE = {"font": ("Courier", 19, "bold"),
                            "bg": "#006989",
                            "fg": "#ffffff",
                            "height": 2}

SCORE_LABEL_STYLE = {"font": ("Courier", 14, "bold"),
                     "bg": "#0096c4",
                     "fg": "#ffffff",
                     "width": 20,
                     "height": 2}

TIMER_LABEL_STYLE = {"font": ("Courier", 14, "bold"),
                     "bg": "#96c400",
                     "fg": "#ffffff",
                     "width": 20,
                     "height": 2
                     }

CURRENT_WORD_LABEL_STYLE = {"font": ("Courier", 18, "bold"),
                            "bg": "#c8c9c3",
                            "fg": "#005b77"}
FOUND_WORDS_LABEL_STYLE = {"font": ("Courier", 14, "bold"),
                           "fg": "#000000"}

class BoggleGUI:
    """GUI for the boggle model"""

    def __init__(self, model):
        """
        Initialize the Gui object with the widgets
        :param model: the BoggleModel to work with
        """
        self.__model = model
        self.__letter_buttons = dict()
        # root
        self.__root = tk.Tk()
        self.__root.title("Boggle")
        self.__root.resizable(False, True)

        # starting frame
        self.__starting_frame = tk.Frame(self.__root)
        self.__starting_message = tk.Label(self.__starting_frame,
                                           text=HELLO_MSG,
                                           **STARTING_LABEL_STYLE)
        self.__sub_start_message = tk.Label(self.__starting_frame,
                                            text=START_GAME,
                                            **SUB_STARTING_LABEL_STYLE)
        self.__start_button = tk.PhotoImage(file="play_game.png").subsample(5)
        self.__restrat_button = tk.PhotoImage(
            file="restart_game.png").subsample(6)
        self.__start_game = tk.Button(self.__starting_frame,
                                      image=self.__start_button,
                                      command=self.start_game)
        # upper frame
        self.__upper_frame = tk.Frame(self.__root, height=30)
        self.__current_word = tk.Label(self.__upper_frame, text="",
                                       **CURRENT_WORD_LABEL_STYLE)
        self.__submit = tk.Button(self.__upper_frame, text=SUBMIT,
                                  command=self.submit, **SUBMIT_BUTTON_STYLE)

        # main_frame
        self.__main_frame = tk.Frame(self.__root)

        # left frame
        self.__left_frame = tk.Frame(self.__main_frame)
        self.__words = tk.Label(self.__left_frame, text="",
                                **FOUND_WORDS_LABEL_STYLE)
        self.__score = tk.Label(self.__left_frame, text="",
                                **SCORE_LABEL_STYLE)
        self.__timer = tk.Label(self.__left_frame, text="",
                                **TIMER_LABEL_STYLE)
        # board frame
        self.__board_frame = tk.Frame(self.__main_frame)

        self.pack()

    def _animate(self):
        """
        This function will take care of the timer
        :return: None
        """
        time = self.__model.get_time()  # get current time
        if not time:  # the timer has ended
            self.finish_game()
        else:
            if not isinstance(time, str):  # check if the time is string
                if time < timedelta(seconds=10):
                    # change the background of the timer
                    self.__timer["bg"] = "#c42e00"
            self.__timer["text"] = TIME_LEFT + str(time)[3:-4]  # Display time
        self.__root.after(10, self._animate)
        # call the function again after 10 mili

    def run(self):
        """
        This function will run the GUI
        :return: None
        """
        self._animate()
        self.__root.mainloop()

    def pack(self):
        """
        This game will pack the widgets for opening screen
        :return: None
        """
        self.__starting_frame.pack()
        self.__starting_message.pack(fill=tk.BOTH, ipadx=20)
        self.__sub_start_message.pack(fill=tk.BOTH)
        self.__start_game.pack(side=tk.BOTTOM, fill=tk.BOTH)

    def start_game(self):
        """
        This function will start the game, unpack all irrelevant widgets and
        pack the relevant widgets
        :return: None
        """
        # unpack the starting screen
        self.__starting_frame.pack_forget()
        self.__starting_message.pack_forget()
        self.__sub_start_message.pack_forget()
        self.__start_game.pack_forget()

        # pack the upper frame
        self.__upper_frame.pack(side=tk.TOP, fill=tk.BOTH)
        self.__submit.pack(side=tk.RIGHT, fill=tk.BOTH, expand=False)
        self.__current_word.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # pack the main frame
        self.__main_frame.pack(fill=tk.BOTH)
        # pack the left frame
        self.__left_frame.pack(side=tk.LEFT, fill=tk.BOTH)
        self.__score.pack(side=tk.BOTTOM)
        self.__timer.pack(side=tk.BOTTOM)
        self.__words.pack(fill=tk.BOTH)

        # pack the board
        self.__board_frame.pack(side=tk.RIGHT)

        self.__model.start_timer()
        self.show_score()
        self.show_word()
        self.add_letters()
        self.__timer["bg"] = "#96c400"
        self.__words["text"] = self.__model.get_correct_words()

    def finish_game(self):
        """
        This function will end the game, unpack all irrelevant widgets and
        pack the relevant widgets
        :return: None
        """
        # pack starting screen
        self.__starting_frame.pack()
        self.__starting_message.pack(fill=tk.BOTH, ipadx=20)
        self.__starting_message["text"] = END_TIME_MSG
        self.__starting_message["bg"] = "#c42e00"
        self.__sub_start_message.pack(fill=tk.BOTH)
        self.__sub_start_message["text"] = SCORE + str(
            self.__model.get_score())
        self.__start_game.pack(fill=tk.BOTH)
        self.__start_game["image"] = self.__restrat_button

        # unpack all game widgets
        self.remove_letters()
        self.__model.initialize_all()
        self.__upper_frame.pack_forget()
        self.__current_word.pack_forget()
        self.__main_frame.pack_forget()
        self.__left_frame.pack_forget()
        self.__board_frame.pack_forget()
        self.__words.pack_forget()
        self.__submit.pack_forget()
        self.__score.pack_forget()
        self.__timer.pack_forget()

    def add_letters(self):
        """
        This functions will add the letter buttons
        :return: None
        """
        board = self.__model.get_board()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self._make_button(board[i][j], i, j)

    def remove_letters(self):
        """
        This function will remove the letter buttons from the screen
        and from the list
        :return: None
        """
        for btn in self.__letter_buttons:
            self.__letter_buttons[btn].grid_forget()
        self.__letter_buttons = dict()

    def _make_button(self, letter, row, col):
        """
        This function will make buttons and bind its commands
        :param letter: The letter that chould be apear on the button
        :param row: in the grid
        :param col: in the grid
        :return: None
        """
        button = tk.Button(self.__board_frame, text=letter,
                           **LETTER_BUTTON_STYLE)
        button.grid(row=row, column=col)
        self.__letter_buttons[letter] = button

        def _on_enter(event) -> None:
            """
            This function will change the background color of the button
            when the mouse enter the button
            :param event: event
            :return: None
            """
            button['background'] = BUTTON_HOVER_COLOR

        def _on_leave(event) -> None:
            """
            This function will change the background color of the button
            when the mouse leave the button
            :param event: None
            :return: None
            """
            button['background'] = REGULAR_COLOR

        button.bind("<Enter>", _on_enter)
        button.bind("<Leave>", _on_leave)
        button.bind("<ButtonPress-1>",
                    lambda event, arg=button: self._key_pressed(event, button))

    def _key_pressed(self, event, btn):
        """
        This function will be called when letter button is pressed
        :param event: event
        :param btn: The button that pressed
        :return: None
        """
        cords = (btn.grid_info()["row"], btn.grid_info()["column"])
        self.__model.add_letter_to_current_word(btn["text"], cords)
        self.__current_word[
            "text"] = CURRENT_WORD + " " + self.__model.get_current_word()

    def submit(self):
        """
        This function is called when the cubmit button is called
        :return: None
        """
        msg = self.__model.add_word()[0]
        self.show_score()
        self.__words[
            "text"] = FOUND_WORDS + self.__model.get_correct_words()
        self.show_word(msg)

    def show_word(self, msg=""):
        """
        This function will show the current word that the user is working on it
        :param msg: if other message is wanted to be displayed
        :return: None
        """
        if not msg:
            self.__current_word["text"] = self.__model.get_current_word()
        else:
            self.__current_word["text"] = msg

    def show_score(self):
        """
        This function will show the current score
        :return: None
        """
        self.__score["text"] = SCORE + str(self.__model.get_score())
