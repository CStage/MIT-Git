# Problem Set 5: 6.00 Word Game
# Name:
# Collaborators:
# Time:
#

import random
import string
import time
import itertools
import operator


VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

inFile = open(WORDLIST_FILENAME, 'r')
# wordlist: list of strings
wordlist = []
for line in inFile:
    wordlist.append(line.strip().lower())

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    print ("  ", len(wordlist), "words loaded.")
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

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    points=0
    if len(word)==0:
        points==0
    if len(word)==n:
        points+=50
    for letter in word:
        #print(letter)
        points+=SCRABBLE_LETTER_VALUES[letter]
        #print(points)
        #print(points)
    return points




"""
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    # TO DO ...

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end='')              # print all on the same line
    print()                              # print an empty line


#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = int(n / 3)

    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not mutate hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    # TO DO ...
    for letter in word:
        hand[letter]-=1
    #print("letter: ", letter, "hand: ", hand)
    return hand


update_hand({'a':1, 'x':2, 'l':3, 'e':1}, "axe")

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    # TO DO ...
#Stolen from the internet - .copy takes a copy of the input and saves it to something
#else. This makes it so that when we delete elements of our hand later we can still
#revert back to the original hand.
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    local_hand=hand.copy()
    wordlist=[]
    for line in inFile:
        wordlist.append(line.strip().lower())
    for letter in word:
        if local_hand.get(letter,0)==0:
#            print("1stfalse")
            return False
        else:
            local_hand[letter]-=1

    if word in wordlist:
#        print("1sttrue")
        return True
    else:
#        print("2ndfalse")
        return False

#is_valid_word("mellow",{'m': 1, 'e': 1, 'l': 2, 'o': 1, 'w':1}, WORDLIST_FILENAME)
#
# Problem #4: Playing a hand
#
def get_words_to_points(word_list):
    """
    Return a dict that maps every word in word_list to its point value.
    """
    points={}
    value=0
    for line in word_list:
        value=get_word_score(line, len(line)-50)
        points[line]=int(value)
    #print(points)
    return points

points_dict=get_words_to_points(wordlist)

def get_time_limit(points_dict, k):
    """
 Return the time limit for the computer player as a function of the
multiplier k.
 points_dict should be the same dictionary that is created by
get_words_to_points.
"""

    start_time = time.time()
# Do some computation. The only purpose of the computation is so we can
# figure out how long your computer takes to perform a known task.
    for word in points_dict:
        get_frequency_dict(word)
        get_word_score(word, HAND_SIZE)
    end_time = time.time()
    print("Time to do task =", end_time-start_time*k)
    return (end_time - start_time) * k


def all_combos(list):
    Combos=[]
    for i in range(len(list)):
        #str1+="".join(i)
        #print("str1: ", str1)
        Combos+=[''.join(p) for p in itertools.permutations(list, i+1)]
        #print("Mid-Permutation: ", [''.join(p) for p in itertools.permutations(list, i+1)])
    #print("Combos", Combos)
    return Combos

def play_best_word(hand, points_dict):
    Actual_moves={}
    maximum=0
    hand_list=[]
    combos=[]
    for letter in hand:
        while hand[letter]>0:
            hand_list.append(letter)
            hand[letter]+=-1
    #print(hand_list)
    combos=all_combos(hand_list)
    #print(combos)
    for line in combos:
        if line in points_dict:
            Actual_moves[line]=points_dict[line]

    if len(Actual_moves)>0:
        best_play=str(max(Actual_moves.items(), key=operator.itemgetter(1))[0])
        #print(Actual_moves)
    else:
        best_play="."

    #print(best_play)

    return best_play
    #print(Actual_moves)

play_best_word({'m': 1, 'e': 1, 'a': 2, 'g': 1, 'r':1, 'n':1}, points_dict)





def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.

    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand
      are displayed, and the user is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    * The final score is displayed.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """
    # TO DO ...
    local_hand=hand.copy()
    start_time=time.time()
    score=0
    elapsed=0
    while elapsed<8:
        num_in_hand=0
        for key in hand.keys():
            for i in range(hand[key]):
                num_in_hand+=1
                print(key)
        if num_in_hand<1:
            break
        play=play_best_word(local_hand, points_dict)
        print("This is the play:", play)
        print("")
        end_time=time.time()
        total_time=end_time-start_time
        if total_time<1:
            total_time+=1


        if play=='.':
            break
        elapsed=time.time()-start_time
        if elapsed>=8:
            print('%.2f' % elapsed, "Seconds have passed. Game over.")
            break
        #print("play", play, "hand", hand)
        if is_valid_word(play, hand, word_list)==True:
            print("It took", '%.2f' % total_time, "to provide an answer")
            print("You have", '%.2f' % (8-elapsed), "seconds remaining")
            print("")
            #print("the calculation:", time.time(), "minus", start_time, "equals", elapsed)
            update_hand(hand, play)
            hand_score=(get_word_score(play, num_in_hand)/total_time)
            score+=hand_score
            print ("Score: ", '%.2f' % hand_score, "Total Score: ", '%.2f' % score)
        else:
            print("Invalid word. Try again.")
        #print(elapsed)
    print("Final score", '%.2f' % score)





play_hand({'m': 1, 'e': 1, 'l': 2, 'o': 1, 'w':1}, WORDLIST_FILENAME)

#
# Problem #5: Playing a game
# Make sure you understand how this code works!
#
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    # TO DO ...



    ## uncomment the following block of code once you've completed Problem #4
    hand = deal_hand(HAND_SIZE) # random init
    while True:
        cmd = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand.copy(), word_list)
            print
        elif cmd == 'r':
            play_hand(hand.copy(), word_list)
            print
        elif cmd == 'e':
            break
        else:
            print("Invalid command.")

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
