""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string
import operator


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    book = open(file_name, 'r')
    lines = book.readlines()
    curr_line = 0

    #cutting out lines before the start of the book
    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
      curr_line += 1
    lines = lines[curr_line+1:]

    # cutting out lines that are at the end of the book
    while lines[curr_line-1].find('END OF THIS PROJECT GUTENBERG EBOOK') == -1:
        curr_line = curr_line - 1
    lines = lines[:curr_line-1]

    #remove punctuation and white space character
    words = ''.join(lines)
    for symbol in string.punctuation:
        words = words.replace(symbol, '')
    editedwords= words.replace('\r', '')

    editedwords = editedwords.lower()
    finalwords = editedwords.split()
    return finalwords

def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """
    histogram = {}
    for word in word_list:
        histogram[word] = histogram.get(word, 0) + 1

    #http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value
    sorted_words = sorted(histogram.items(), key=lambda x:x[1], reverse=True)
    main_words = sorted_words[:n]
    return main_words


if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    print(get_top_n_words(get_word_list('douglass.txt'),100))
