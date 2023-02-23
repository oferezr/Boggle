from boggleGui import *
from models.bogglemodel import *


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
