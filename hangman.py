from collections import Counter
from gallows import game_gallows

# Frequency of letters in English words (most common to least common)
letter_frequency = "etaoinshrdlcumwfgypbvkjxqz"

def ai_guess(guessed_letters):
    for letter in letter_frequency:
        if letter not in guessed_letters:
            guessed_letters.add(letter)
            return letter
    return None

def display_word_state(phrase, guessed_letters):
    displayed_word = ""
    for char in phrase:
        if char in guessed_letters:
            displayed_word += char + " "
        else:
            displayed_word += "_ "
    print(displayed_word.strip())

def get_letter_guess():
    while True:
        guess = input("Please guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You have already guessed that letter. Try again.")
            else:
                guessed_letters.add(guess)
                return guess
        else:
            print("Invalid input. Please enter a single letter.")

def hangman_game():
    print("\033[1mWelcome to hangman!\033[0m")
    user_input = input("""If you would like to know the rules please enter '?', 
otherwise simply press Enter to continue: """)
    if user_input == '?':
        print("""
        The objective of the game is to guess the hidden word, one letter at a time, before the entire man is 'hanged'. 
        - You will be presented with a series of blanks representing the letters in the hidden word.
        - Each time you guess a correct letter, it will be revealed in its correct position(s).
        - If you guess a wrong letter, a part of the gallows or the man will be drawn.
        - You have a limited number of incorrect guesses before the game is over.

        Good luck, and have fun!
        """)

    phrase = input("What is the word:").lower()
    guessed_letters = set()
    gallownum = 0

    while gallownum < 6:
        print(game_gallows[gallownum])
        display_word_state(phrase, guessed_letters)
        
        game_mode = input("Do you want to guess (G) or let the AI guess (A)? ").lower()
        if game_mode == 'g':
            guess = get_letter_guess()
        else:
            guess = ai_guess(guessed_letters)
            print(f"AI guesses: {guess}")

        if guess in phrase:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            gallownum += 1

        if all(char in guessed_letters for char in phrase):
            print("Congratulations! You've guessed the word!")
            break
    else:
        print(game_gallows[gallownum])
        print(f"You've run out of guesses. The word was '{phrase}'.")

    print("Thanks for playing!")

# Run the game
hangman_game()

