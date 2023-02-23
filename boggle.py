# ##########################
# FILE:boggle.py
# WRITER:Ofer Ezrachi,oferezr, 209350586
# WRITER:Bar Cavia, barcavia123, 316032622
# EXERCISE: intro2cs1 ex12 2021
# DESCRIPTION: The boggle game
# ##########################

from boggleGui import *
from bogglemodel import *


class Boggle:
    """
    Boggle game
    """
    def __init__(self, filename):
        """
        This function will create new boggle game instance
        :param filename: the dictionary to read the word from
        """
        words = load_words_dict(filename)
        self.__model = BoggleModel(words)
        self.__boggleGUI = BoggleGUI(self.__model)

    def run(self):
        """
        This word will run the boggle game
        :return: None
        """
        self.__boggleGUI.run()


if __name__ == '__main__':
    game = Boggle("assets/boggle_dict.txt")
    game.run()
