

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string
from hangmanClass import Word
from hangmanClass import Guess


# end of helper code
# -----------------------------------
# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program

wordObject = Word()

wordlist = wordObject.load_words()
print ("\n\n\t\tWelcome to the game, Hangman! ".upper())

    # your code begins here!
word = wordObject.choose_word(wordlist)

length = len(word)
max_attempts = length + 1
available_letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
        

    # Print game headers 
    ##print word
print ("  I am looking for a word that contains", length, " letters")
print ("  ---------------")
print ("  You have", max_attempts, "guesses to make.")
print ("  Available letters: ", available_letters)
   
guessObject = Guess()

guess = guessObject.get_guess()

guessObject.eval_guess(guess,word, length)
