import random
import string
class Hangman():

    def Playing(self,WORDLIST):
        WORDLIST = "words.txt"
        inFile = open(WORDLIST_FILENAME, 'r')
        line = inFile.readline()
        wordlist = line.split()
        return wordlist

        tryagain = True
        while tryagain:

            guessWord = random.choice(WORDIST)
            board = "*" * len(guessedWord)
            alreadySaid = set()
            attempts = 7

            print("_".join(board))

            guessed = False
            while not guessed and attempts > 0:

                chosen = input("Guess a letter: ")

                if chosen in guessWord:
                    alreadySaid.add(chosen)
                    board = "".join([char if char in alreadySaid else "*" for char in guessWord])
                    if board == guessWord:
                        guessed = True
                else:
                    attempts -= 1
                    print("Nope.", attempts, "attempts left.")

                print(" ".join(board))

            again = (input("Again [y/n]: ").lower() == 'y')

#----------------------------------------------------------------------

Hangman().Playing()
