# ##########################
# FILE:bogglemodel.py
# WRITER:Ofer Ezrachi,oferezr, 209350586
# WRITER:Bar Cavia, barcavia123, 316032622
# EXERCISE: intro2cs1 ex12 2021
# DESCRIPTION:This file contain the logics behind the boggle game
# ##########################

from datetime import datetime, timedelta

from boggle_board_randomizer import randomize_board
from ex12_utils import *


class BoggleModel:
    """Logic part of the game"""
    NOT_EXIST_MSG = "No Word Such That"
    DUPLICATE_WORDS_MSG = "You Have Already Found This Word"
    WORD_FOUND_MSG = "Nice!"
    MAX_WORD_LEN = 16

    def __init__(self, words):
        """
        :param words: the valid dictionary of the words
        """
        self.__game_end_time = None
        self.__current_path = []
        self.__current_word = ""
        self.__score = 0
        self.__correct_words = []
        self.__board = randomize_board()
        self.__words_dict = words

    def get_score(self):
        """
        :return: user's score
        """
        return self.__score

    def get_time(self):
        """
        :return: Time or false if its bigger then 3:00
        """
        if self.__game_end_time:
            delta = self.__game_end_time - datetime.now()
            if '-' in str(delta):
                return False
            return delta
        return "00:00"

    def start_timer(self):
        """
        :return: returns the timer to the GUI
        """
        self.__game_end_time = datetime.now() + timedelta(minutes=3)

    def get_board(self):
        """
        :return: returns the board to the GUI
        """
        return self.__board

    def get_correct_words(self):
        """
        :return: the correct words that the user found
        """
        str_correct_words = '\n'.join(map(str, self.__correct_words))
        return str_correct_words

    def initialize_parameters(self):
        """
        :return: None. just initialize the current word and the current path.
        the function will be activated when the user found a correct word
        """
        self.__current_word = ""
        self.__current_path = []

    def add_word(self):
        """
        :return: the current word to the GUI. the word can be a msg, or the
        word itself, in case the user was correct
        the function adds a word, updates the score and clears the used_letters
        """
        if is_valid_path(self.__board, self.__current_path, self.__words_dict):
            if self.__current_word not in self.__correct_words:
                self.__correct_words.append(self.__current_word)
                self.__score += len(self.__current_word) ** 2
                self.__current_word = self.WORD_FOUND_MSG
                return self.__current_word, self.initialize_parameters()
            else:
                self.__current_word = self.DUPLICATE_WORDS_MSG
                return self.__current_word, self.initialize_parameters()
        else:
            self.__current_word = self.NOT_EXIST_MSG
            return self.__current_word, self.initialize_parameters()

    def get_current_word(self):
        """
        :return: returns the current sequence of the word, in order to display
        it on the GUI
        """
        return self.__current_word

    def add_letter_to_current_word(self, letter, cords):
        """
        :param letter: a given letter from the GUI
        :param cords: given coordinates from GUI
        :return: None. just adds the letter to the current word and its
        coordinates to the path, in order to
        check if the final path (after the user submitted a word) is valid.
        """
        if len(self.__current_word) <= self.MAX_WORD_LEN:
            self.__current_word += letter
            self.__current_path.append(cords)

    def initialize_all(self):
        """
        :return: None. the function will be activated in case the user decided
        to plat again
        """
        self.__game_end_time = None
        self.__current_path = []
        self.__current_word = ""
        self.__score = 0
        self.__correct_words = []
        self.__board = randomize_board()
