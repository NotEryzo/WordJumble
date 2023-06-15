# Word Jumble Game using OOP by Sami

import random

# Class function with constructor and parameters
class WordJumbleGame:
    def __init__(self, words):
        self.words = words
        self.total_words = len(words)
        self.score = 0
    
    # Shuffles the words
    def shuffleword(self, word):
        shuffled_word = list(word)
        random.shuffle(shuffled_word)
        return "".join(shuffled_word)

    # The main function where every time a word is reassembled correctly it will get removed from the array so that it doesn't appear twice. 
    def play(self):
        playing = True
        while playing and len(self.words) > 0:
            word = random.choice(self.words)
            shuffled_word = self.shuffleword(word)

            guess_count = 0
            round_over = False
            while not round_over:
                print("Guess the word:", shuffled_word)

                guess = input("Enter your guess (or 'quit' to exit): ")

                if guess.lower() == "quit":
                    round_over = True
                    playing = False
                elif guess.lower() == word:
                    self.score += 1
                    self.words.remove(word)
                    print("Congratulations! You guessed the word correctly.")
                    round_over = True
                else:
                    guess_count += 1
                    print("Incorrect guess. Try again.")

                if guess_count == 3:
                    print("Out of guesses! The word was:", word)
                    round_over = True

            print("Your score:", self.score)

            if self.score == self.total_words:
                print("Congratulations! You have guessed all the words correctly. You win!")
                playing = False

            if playing and len(self.words) > 0:
                play_again = input("Do you want to play again? (yes/no): ")
                if play_again.lower() != "yes":
                    playing = False

        print("Thank you for playing! Final score:", self.score)

# Array of words
words = ["apple", "banana", "cherry", "orange", "strawberry"]

# Start the game
game = WordJumbleGame(words)
game.play()
