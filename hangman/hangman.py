# Import modules
import os
import random
from string import ascii_letters

# Define a list of words
words = ["tiger", "elephant", "giraffe", "zebra", "lion"]

# Define the maximum number of attempts
max_attempts = 6

# Initialize the number of attempts
attempts = 6

# Define a function to pick a random word
def pick_word(words):
    return random.choice(words)

# Pick a random word and store it in a variable
word = pick_word(words)

# Define a function to display the hangman
def display_hangman(attempts):
    # Define a list of hangman stages
    stages = ["""
  ------
  |    |
  |    O
  |   /|\\
  |   / \\
  |
  ------------
  """,
  """
  ------
  |    |
  |    O
  |   /|\\
  |   /
  |
  ------------
  """,
  """
  ------
  |    |
  |    O
  |   /|\\
  |
  |
  ------------
  """,
  """
  ------
  |    |
  |    O
  |    |
  |
  |
  ------------
  """,
  """
  ------
  |    |
  |    O
  |
  |
  |
  ------------
  """,
  """
  ------
  |    |
  |
  |
  |
  |
  ------------
  """]

    # Clear the screen
    os.system("clear")

    # Print the hangman stage based on the number of attempts left
    print(stages[max_attempts - attempts])

    # Define a function to display the word
def display_word(word, guessed_letters):
    # Create a list of underscores for each letter in the word
    blanks = ["_" if letter not in guessed_letters else letter for letter in word]

    # Join the list with spaces and print it
    print(" ".join(blanks))

    # Print the number of attempts left
    print(f"You have {attempts} attempts left.")

    # Print the guessed letters
    print(f"You have guessed these letters: {guessed_letters}")

    # Define a function to get the user's input
def get_input(guessed_letters):
    # Get the user's input and convert it to lowercase
    guess = input("Guess a letter: ").lower()

    # Check if the input is a single letter
    if len(guess) != 1 or guess not in ascii_letters:
        print("Invalid input. Please enter a single letter.")
        return get_input(guessed_letters)

    # Check if the input is not in the list of guessed letters
    if guess in guessed_letters:
        print("You have already guessed that letter. Try another one.")
        return get_input(guessed_letters)

    # Return the input if it's valid
    return guess

# Initialize the list of guessed letters
guessed_letters = ""

# Start the main loop
while True:
    # Display the hangman and the word
    display_hangman(attempts)
    display_word(word, guessed_letters)

    # Get the user's input
    guess = get_input(guessed_letters)

    # Add the input to the list of guessed letters
    guessed_letters += guess

    # Check if the input is in the word
    if guess in word:
        # Print a message saying that the user guessed correctly
        print(f"Good guess! {guess} is in the word.")
    else:
        # Print a message saying that the user guessed wrong
        print(f"Sorry, {guess} is not in the word.")

        # Reduce the number of attempts by one
        attempts -= 1

    # Check if the user has guessed all the letters in the word
    if all(letter in guessed_letters for letter in word):
        # Print a message saying that the user won
        print(f"Congratulations! You guessed the word: {word}")

        # Break the loop
        break

    # Check if the user has no more attempts left
    if attempts == 0:
        # Print a message saying that the user lost
        print(f"You ran out of attempts. You lost. The word was: {word}")

        # Break the loop
        break