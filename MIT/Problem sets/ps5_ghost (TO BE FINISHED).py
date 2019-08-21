# Problem Set 5: Ghost
# Name:
# Collaborators:
# Time:
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print( "  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

# TO DO: your code begins here!

def Allowed_Move(word, wordlist):
#    print(word)
    if len(word)>10:
#        print("Words.txt only holds words of max 10 letters. Game over.")
#        print("")
        return False
    if word in wordlist:
        if len(word)<=3:
#            print(word, "is a real word, but it's only 3 characters, so we cool")
#            print("")
            return True
        if len(word)==10:
#            print(word, "is a real word, but we're at the 10th key, so you win!")
#            print("")
            return True
        else:
#            print(word, "is a real word. You lose")
#            print("")
            return False

    for line in wordlist:
        if word in line and len(word)<len(line):
#            print("Great move", word, "is allowed")
#            print("")
            return True
    else:
#        print("You cannot create a word from", word, "you lose.")
#        print("")
        return False


def ghost(wordlist):
    current_word=str("")
    while len(current_word)<10:
        while True:
            print("")
            play1=str(input("Player 1 - Input a character: "))
            if not len(play1)==1:
                print("Input MUST be 1 (one) character long")
            else:
                break
        current_word+=play1
        if Allowed_Move(current_word, wordlist):
            print(play1, "is allowed.")
            print("Current word is", current_word)
            print("")
            while True:
                print("")
                play2=str(input("Player 2 - Input a character:"))
                if not len(play2)==1:
                    print("Input MUST be 1 (one) character long")
                else:
                    break
            current_word+=play2
            if Allowed_Move(current_word, wordlist):
                print(play2, "is allowed")
                print("Current word is", current_word)
            else:
                print("Not allowed. Player 2 loses")
                return None
        else:
            print("Not allowed. Player 1 loses")
            return None

ghost(wordlist)
