import random 
import string


class Word ():
    WORDLIST_FILENAME = "words.txt"
   # def __init__ (self,guess):
     #   self.guessoblect = Guess()

        
    
    def choose_word(self, wordlist):
        return random.choice(wordlist)


    def load_words(self):
        inFile = open(self.WORDLIST_FILENAME, 'r')
        line = inFile.readline()
        wordlist = line.split()
        return wordlist

class Guess ():


    def del_alphabeth(self, alphabeth,choice_range):
        if alphabeth in choice_range:
           letters_remaining = choice_range.replace(alphabeth,"_ ")
           return letters_remaining
        

    def progress_so_far(self, word,guessed_letters):
        newstring = []
        for index in range(len(word)):
            letters = word[index]
            if letters in guessed_letters:
                newstring.append(letters)
            else:
                newstring.append("_")
        return newstring
    

    def get_guess(self):
        guess =input("\n\n  Please guess a letter: ").lower()
        return guess


    def eval_guess(self, guess, word, length):
        max_attempts = length + 1
        available_letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
        guessed_letters = []
        newstring = []
        correct_guesses = 0
        wrong_guesses = 0

        while True  and max_attempts > 1:
            # Ensures that only a single alphabeth is entered at a time 
            if (guess == '' or len(guess) > 1) : # 
                print ( "  Guess must be a single letter !")
                guess = self.get_guess()
            # Prevents guessing any letter more than once
            if guess in guessed_letters:
                print( " This letter has been guessed!")
                guess = self.get_guess()
                
            else:
                guessed_letters.append(guess)
                # performs the actual check for the guessed letter in the word

                if guess not in word:
                    print ("   Opps!", guess, "is not in the word")
                    print ("   -----------------")
                    max_attempts -= 1  
                    print ("  you have ", max_attempts, "attempts left")
                    available_letters = self.del_alphabeth(guess, available_letters)
                    print ("  Available letters: ", available_letters)
                    wrong_guesses += 1
                    guess = self.get_guess()

                else:  
                    print ("   Good guess: '", guess, "' appeared", word.count(guess), "times")
                    print ("   progress so far: ", self.progress_so_far(word,guessed_letters))
                    available_letters = self.del_alphabeth(guess,available_letters)
                    print ("\n  Available Letters:  ", available_letters)

                    correct_guesses += word.count(guess) # gets 
                    if  correct_guesses == length:
                        print (" \n\n\t\t Great Job! the word is ", word.upper(), "!!!")
                        print ("\t\t wrong guesses: ",wrong_guesses)
                        break
                    else:
                        guess = self.get_guess()
        else:
            print ("\n\t ************************************")
            print ("\t\t\t\tGame Over!".upper()) # terminate the game
            print ("\t ************************************")
            print ("\n\t\t The word is ", word.upper())
            exit()

