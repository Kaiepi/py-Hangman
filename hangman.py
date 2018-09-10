#!/usr/bin/env python3
from random import randint

class Hangman:

    """
    self.target        - the progress of the guessed word
    self.guessed       - guessed letters and words
    self.wrong_answers - number of mistakes made, a maximum of 6 allowed
    self.ended         - whether or not the game is finished
    self.__word        - the full word you're attempting to guess
    """

    def __init__(self):
        self.target        = ''
        self.guessed       = set()
        self.wrong_answers = 0
        self.ended         = False
        self.__word        = ''

    def run(self):
        while True:
            print('The Hangman game has started!')
            self.get_random_word()
            self.update_word()
            while not self.ended:
                self.print_info()
                guess = self.get_guess()
                self.check_guess(guess)
                print()

            response = ''
            while response != 'y' and response != 'n':
                response = input('Would you like to play again? [y/n]: ')
            if response == 'y':
                self.reset()
                print()
            else:
                break

    def reset(self):
        self.target = ''
        self.guessed.clear()
        self.wrong_answers = 0
        self.ended = False
        self.__word = ''

    def get_random_word(self):
        with open('dictionary', 'r') as f:
            lines = f.readlines()
            idx = randint(0, len(lines))
            self.__word = lines[idx].rstrip()

    def update_word(self):
        output = []
        for ch in self.__word:
            if ch in self.guessed:
                output.append(ch)
            else:
                output.append('_')
        self.target = ''.join(output)

    def print_info(self):
        print(self.target)
        guessed = sorted(self.guessed)
        guessed = ' '.join(guessed)
        print(f'Guessed: {guessed}')

    def get_guess(self):
        guess = '';
        while guess == '':
            guess = input('Guess a letter or word: ')
            guess = guess.upper()
        return guess

    def check_guess(self, guess):
        if guess in self.guessed:
            print(f'{guess} has already been guessed.')
            return False

        if len(guess) > 1 and len(guess) < len(self.__word):
            print(f'{guess} does not match the current word.')
            return False

        if len(guess) == 1:
            self.guessed.add(guess)

        if guess not in self.__word:
            print(f'{guess} is not in or is not the current word.')
            if self.wrong_answers < 5:
                self.wrong_answers += 1
                print(f'You currently have {6 - self.wrong_answers} wrong answers remaining.')
            else:
                self.ended = True;
                print(f'You have lost the game. The word was {self.__word}.')
            return False

        print(f'You correctly guessed {guess}!')
        self.update_word()
        if self.target == self.__word or guess == self.__word:
            self.ended = True
            print('You have won the game!')
        return True

if __name__ == '__main__':
    hangman = Hangman()
    hangman.run()
