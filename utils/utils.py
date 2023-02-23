# ##########################
# FILE:utils.py
# WRITER:Ofer Ezrachi,oferezr, 209350586
# WRITER:Bar Cavia, barcavia123, 316032622
# EXERCISE: intro2cs1 ex12 2021
# DESCRIPTION: This file contain helper functions for the boggle game
# ##########################

from itertools import permutations, combinations

NEW_LINE = '\n'
EMPTY_CHAR = ''
ROW = 0
COL = 1
BOARD_SIZES = 4
COORDINATES = [(x, y) for x in range(BOARD_SIZES) for y in range(BOARD_SIZES)]


def load_words_dict(file_path):
    """
   :param file_path: a given path that contains the game words
   :return: a dictionary containing all the words
   """
    words_dict = {}
    with open(file_path) as file:
        for line in file.readlines():
            temp_line = line.replace(NEW_LINE, EMPTY_CHAR)
            if temp_line not in words_dict:
                words_dict[temp_line] = True
        return words_dict


def is_valid_path(board, path, words):
    """
   :param board: the board game
   :param path: a given path on the board representing an optional exciting word
   :param words: the valid dictionary of the words
   :return: the word if the path was valid, else returns None
   """
    if not path:
        return
    if duplicate_cords_in_path(path):
        return
    if valid_cords(path, len(board)):
        temp_word = get_letter_in_board(path[0], board)
        pre_cords = path[0]
        for cords in path[1:]:
            if check_valid_path(pre_cords, cords):
                temp_word += get_letter_in_board(cords, board)
                pre_cords = cords
            else:
                return
        return word_from_path_in_dict(temp_word, words)
    return


def check_valid_path(pre_cords, cur_cords):
    """
   :param pre_cords: the previous coordinates in the path
   :param cur_cords: the current coordinates in the path
   :return: True if the the path is valid due to the optional directions
   """
    return 0 <= abs(cur_cords[ROW] - pre_cords[ROW]) <= 1 and 0 <= abs(
        cur_cords[COL] - pre_cords[COL]) <= 1


def get_letter_in_board(cords, board):
    """
   :param cords: coordinates as a tuple
   :param board: game board
   :return: The letter in the cords on the board
   """
    for i in range(len(board)):
        for j in range(len(board)):
            if i == cords[0] and j == cords[1]:
                return board[i][j]


def word_from_path_in_dict(word, words_dic):
    """
   :param word: word from a given path
   :param words_dic: words dictionary
   :return: the word if its in the dictionary, else None
   """
    if word in words_dic:
        return word
    return


def valid_cords(cords, board_len):
    """
   :param cords: coordinates of a given path
   :param board_len: the game board
   :return: True if the cords is valid
   """
    for cord in cords:
        if cord[ROW] >= board_len or cord[COL] >= board_len:
            return False
        if cord[ROW] < 0 or cord[COL] < 0:
            return False
    return True


def duplicate_cords_in_path(path):
    """
    :param path: a given path in the board
    :return: True if the user used a letter twice
    """
    if len(set(path)) == len(path):
        return False
    return True


def find_length_n_words(n, board, words):
    """
   :param n: the word length
   :param board: the board game
   :param words: the valid dictionary of the words
   :return: a list of tuples representing a valid word, and its path on the board
   """
    paths_permutations = all_permutations(COORDINATES, n)
    sub_paths = [tuple(item) for item in paths_permutations]
    results = []
    for path in sub_paths:
        check_word = is_valid_path(board, list(path), words)
        if check_word:
            results.append((check_word, list(path)))
    if not results:
        return []
    return results


def all_permutations(lst, n):
    """
    :param lst: a list of the board coordinates
    :param n: the word length
    :return: all the possible coordinates that representing the possibe paths
    """
    if n <= 0:
        return [[]]
    else:
        new_lst = []
        one_letter = all_permutations(lst, n - 1)
        for item in one_letter:
            for cor in lst:
                if not item:
                    new_lst.append([cor] + item)
                elif check_valid_path(cor, item[0]):
                    if cor != item[0]:
                        new_lst.append([cor] + item)
        return new_lst

