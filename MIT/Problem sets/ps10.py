# Backend code for PS10

import random
import string
import itertools
import operator

# Global Constants
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 30
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
HUMAN_SOLO = 0
HUMAN_VS_HUMAN = 1
HUMAN_VS_COMP = 2

WORDLIST_FILENAME = "words.txt"

def getFrequencyDict(sequence):
    """
    Given a sequence of letters, convert the sequence to a dictionary of
    letters -> frequencies. Used by containsLetters().

    returns: dictionary of letters -> frequencies
    """
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

def getWordScore(word):
    """
    Computes the score of a word (no bingo bonus is added).

    word: The word to score (a string).

    returns: score of the word.
    """
    score=0
    if len(str(word))==0:
        score==0
    if len(str(word))==HAND_SIZE:
        score+=50
    for letter in str(word):
        if word==".":
            break
        if letter=="N":
            letter="n"
        #print(letter)
        score+=SCRABBLE_LETTER_VALUES[letter]
#        print("word: ", word)
#        print(letter)
        #print(points)
        #print(points)
#    print(score)
    return score

def all_combos(list):
    Combos=[]
    length=1
    while length<=10:
        for i in range(len(list)):
            #str1+="".join(i)
            #print("str1: ", str1)
            Combos+=[''.join(p) for p in itertools.permutations(list, length)]
#            print("combos", Combos)
            #print("Mid-Permutation: ", [''.join(p) for p in itertools.permutations(list, i+1)])
            length+=1
#    print("Combos", Combos)
    return Combos



def get_words_to_points(word_list):
    """
    Return a dict that maps every word in word_list to its point value.
    """
    points={}
    value=0
    for line in word_list:
        value=getWordScore(line)
        points[line]=int(value)
    #print(points)
    return points

inFile = open(WORDLIST_FILENAME, 'r')
# wordlist: list of strings
wordlist = []
for line in inFile:
    wordlist.append(line.strip().lower())
points_dict=get_words_to_points(wordlist)

def play_best_word(hand, points_dict):
    Actual_moves={}
    maximum=0
    hand_list=[]
    combos=[]
    for letter in hand:
        while hand[str(letter)]>0:
            hand_list.append(letter)
            hand.update({str(letter):hand[letter]-1})
    #print(hand_list)
    combos=all_combos(hand_list)
#    print("combos", combos)
    #print(combos)
    for line in combos:
        if line in points_dict:
            Actual_moves[line]=points_dict[line]

    if len(Actual_moves)>0:
        best_play=str(max(Actual_moves.items(), key=operator.itemgetter(1))[0])
        #print(Actual_moves)
    else:
        best_play="."

#    print("best play", best_play)

    return best_play
    #print(Actual_moves)

#
# Problem 2: Representing a Hand
#

class Hand(object):
    def __init__(self, handSize, initialHandDict = None):
        """
        Initialize a hand.

        handSize: The size of the hand

        postcondition: initializes a hand with random set of initial letters.
        """
        num_vowels = int(handSize / 3)
        if initialHandDict is None:
            initialHandDict = {}
            for i in range(num_vowels):
                x = VOWELS[random.randrange(0,len(VOWELS))]
                initialHandDict[x] = initialHandDict.get(x, 0) + 1
            for i in range(num_vowels, handSize):
                x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
                initialHandDict[x] = initialHandDict.get(x, 0) + 1
        self.initialSize = handSize
        self.handDict = initialHandDict
        self.members=[]
        self.values=initialHandDict
        self.more=None
    def update(self, word):
        """
        Remove letters in word from this hand.

        word: The word (a string) to remove from the hand
        postcondition: Letters in word are removed from this hand
        """
        # TODO
        self.word=word
#        print("Original dict", self.handDict)
        for letter in self.word:
            if self.handDict[letter]>0:
#                print(self.word, letter)
                self.handDict[letter]-=1
#                print(self.handDict)
            else:
#                print("No way")
                return self.handDict
        self.values=self.handDict
        return self.handDict
    def containsLetters(self, letters):
        """
        Test if this hand contains the characters required to make the input
        string (letters)

        returns: True if the hand contains the characters to make up letters,
        False otherwise
        """
        inFile = open(WORDLIST_FILENAME, 'r')
        # wordlist: list of strings
        local_hand=self.handDict.copy()
        wordlist=[]
        for line in inFile:
            wordlist.append(line.strip().lower())
#        print("letters", letters)
        for letter in letters:
            if local_hand.get(letter,0)<=0:
#                print("1stfalse")
                return False
            else:
                local_hand[letter]-=1
            return True

#        if letters in self.handDict:
#            print("1sttrue")
#            return True
#        else:
#            print("2ndfalse")
#            return False
        # TODO



    def isEmpty(self):
        """
        Test if there are any more letters left in this hand.

        returns: True if there are no letters remaining, False otherwise.
        """
        # TODO
#        print("Testing if", self.handDict, "is empty")
        for keys in self.handDict:
            if self.handDict[keys]>0:
                return False
        return True

    def __eq__(self, other):
        """
        Equality test, for testing purposes

        returns: True if this Hand contains the same number of each letter as
        the other Hand, False otherwise
        """
        # TODO
        sum=0
        for keys, values in self.handDict:
            self.sum+=values
        for keys, values in other.handDict:
            other.sum+=values

        if self.sum==other.sum:
            return True
    def __str__(self):
        """
        Represent this hand as a string

        returns: a string representation of this hand
        """
        string = ''
        for letter in self.handDict.keys():
            for j in range(self.handDict[letter]):
                string = string + letter + ' '
        return string
    def __iter__(self):
        self.place=0
        return iter(self.values)
    def __next__(self):
        for i in self.handDict:
            self.members.append(i)
        if self.place >= len(self.handDict):
            raise StopIteration
        else:
            self.place += 1
            return self.members[self.place-1]
    def __getitem__(self, key):
        return self.values[key]
    def keys(self):
        return self.values.keys()
    def items(self):
        return self.values.items()
    def values(self):
        return self.values.values()


#
# Problem 3: Representing a Player
#

class Player(object):
    """
    General class describing a player.
    Stores the player's ID number, hand, and score.
    """
    def __init__(self, idNum, hand):
        """
        Initialize a player instance.

        idNum: integer: 1 for player 1, 2 for player 2.  Used in informational
        displays in the GUI.

        hand: An object of type Hand.

        postcondition: This player object is initialized
        """
        self.points = 0.
        self.idNum = idNum
        self.hand = hand
    def getHand(self):
        """
        Return this player's hand.

        returns: the Hand object associated with this player.
        """
        # TODO
        return self.hand
    def addPoints(self, points):
        """
        Add points to this player's total score.

        points: the number of points to add to this player's score

        postcondition: this player's total score is increased by points
        """
        # TODO
        self.points+=points
        return self.points

    def getPoints(self):
        """
        Return this player's total score.

        returns: A float specifying this player's score
        """
        # TODO
        return float(self.points)

    def getIdNum(self):
        """
        Return this player's ID number (either 1 for player 1 or
        2 for player 2).

        returns: An integer specifying this player's ID number.
        """
        # TODO
        return self.idNum
    def __eq__(self, other):
        """
        Compare players by their scores.

        returns: 1 if this player's score is greater than other player's score,
        -1 if this player's score is less than other player's score, and 0 if
        they're equal.
        """
        # TODO
        return self.points==other.points
    def __lt__(self, other):
        return (self.points<other.points)

    def __str__(self):
        """
        Represent this player as a string

        returns: a string representation of this player
        """
        return 'Player %d\n\nScore: %.2f\n' % \
               (self.getIdNum(), self.getPoints())

#
# Problem 4: Representing a Computer Player
#

class ComputerPlayer(Player):
    """
    A computer player class.
    Does everything a Player does, but can also pick a word using the
    PickBestWord method.
    """
    def pickBestWord(self, wordlist):
        """
        Pick the best word available to the computer player.

        returns: The best word (a string), given the computer player's hand and
        the wordlist
        """
        # TODO
#        print("self.hand", self.hand)
#        self.hand["a"]=1
#        print("self.hand[a]-=1", self.hand["a"])
#        print("in-function best play", play_best_word(self.hand, points_dict))
        return play_best_word(self.hand, points_dict)
#        print(self.hand, wordlist)

    def playHand(self, callback, wordlist):
        """
        Play a hand completely by passing chosen words to the callback
        function.
        """
        while callback(self.pickBestWord(wordlist)): pass

class HumanPlayer(Player):
    """
    A Human player class.
    No methods are needed because everything is taken care of by the GUI.
    """

class Wordlist(object):
    """
    A word list.
    """
    def __init__(self):
        """
        Initializes a Wordlist object.

        postcondition: words are read in from a file (WORDLIST_FILENAME, a
        global constant) and stored as a list.
        """
        inputFile = open(WORDLIST_FILENAME)
        self.members=[]
        try:
            self.wordlist = []
            for line in inputFile:
                self.wordlist.append(line.strip().lower())
        finally:
            inputFile.close()
    def containsWord(self, word):
        """
        Test whether this wordlist includes word

        word: The word to check (a string)

        returns: True if word is in this Wordlist, False if word is not in
        Wordlist
        """
        return word in self.wordlist
    def getList(self):
        return self.wordlist
    def __iter__(self):
        self.place=0
        return self
    def __next__(self):
        for i in self.wordlist:
            self.members.append(i)
        if self.place >= len(self.wordlist):
            raise StopIteration
        else:
            self.place += 1
            return self.members[self.place-1]

class EndHand(Exception): pass

class Game(object):
    """
    Stores the state needed to play a round of the word game.
    """
    def __init__(self, mode, wordlist):
        """
        Initializes a game.

        mode: Can be one of three constant values - HUMAN_SOLO, HUMAN_VS_COMP,
        and HUMAN_VS_HUMAN

        postcondition: Initializes the players nd their hands.
        """
        hand = Hand(HAND_SIZE)
        hand2 = Hand(HAND_SIZE, hand.handDict.copy())
        if mode == HUMAN_SOLO:
            self.players = [HumanPlayer(1, hand)]
        elif mode == HUMAN_VS_COMP:
            self.players = [HumanPlayer(1, hand),
                            ComputerPlayer(2, hand2)]
        elif mode == HUMAN_VS_HUMAN:
            self.players = [HumanPlayer(1, hand),
                            HumanPlayer(2, hand2)]
        self.playerIndex = 0
        self.wordlist = wordlist
    def getCurrentPlayer(self):
        """
        Gets the Player object corresponding to the active player.

        returns: The active Player object.
        """
        return self.players[self.playerIndex]
    def nextPlayer(self):
        """
        Changes the game state so that the next player is the active player.

        postcondition: playerIndex is incremented
        """
        if self.playerIndex + 1 < len(self.players):
            self.playerIndex = self.playerIndex + 1
            return True
        else:
            return False
    def gameOver(self):
        """
        Determines if the game is over

        returns: True if the playerIndex >= the number of players, False
        otherwise
        """
        return self.playerIndex >= len(self.players)
    def tryWord(self, word):
        if word == '.':
            raise EndHand()
        player = self.getCurrentPlayer()
        hand = player.getHand()
        if self.wordlist.containsWord(word) and hand.containsLetters(word):
            points = getWordScore(word)
            player.addPoints(points)
            hand.update(word)
            if hand.isEmpty():
                raise EndHand()
            return points
        else:
            return None
    def getWinner(self):
        return max(self.players)
    def getNumPlayers(self):
        return len(self.players)
    def isTie(self):
        return len(self.players) > 1 and \
               self.players[0].getPoints() == self.players[1].getPoints()
    def __str__(self):
        """
        Convert this game object to a string

        returns: the concatenation of the string representation of the players
        """
        string = ''
        for player in self.players:
            string = string + str(player)
        return string

#p = ComputerPlayer(1, Hand(6, {'c':1, 'a':1, 'b':1 ,'d':1, 'o':1, 'e':1}))
#print("self.hand", p.hand)
print("play_best_word", play_best_word({'c':1, 'a':1, 'b':1 ,'d':1, 'o':1, 'e':1}, points_dict))
#print("pickBestWord", p.pickBestWord(wordlist))
#print(points_dict)
