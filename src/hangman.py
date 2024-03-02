import draw
import random
import sys
import words
import os

print(draw.logo, "\n")

# Randomly choose a word from the word_list
chosen_word = random.choice(words.word_list)

# Generate blank letters for chosen_word
blank_letters = []
for _ in chosen_word:
    blank_letters += "_"


def hangman():
    used_lives = 7
    game_over = False
    wrong_letter = []

    while not game_over:
        # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
        try:
            print(draw.hangman_stages[used_lives])
            print("".join(blank_letters))
            guess = input("Guess a letter: ").lower()
            os.system("clear")

            if guess in blank_letters:
                print(f"You\'ve already typed '{guess}'.")

            if guess in wrong_letter:
                print(f"You\'ve already tried the letter '{guess}'.")

            # Check if guess is one of the letters in the chosen_word.
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    blank_letters[i] = chosen_word[i]

            # Track the count of lives used
            if guess not in chosen_word:
                if guess not in wrong_letter:
                    wrong_letter += guess
                    used_lives -= 1
                    print(f'"{guess}" is not in the word, try again. 🤷‍')

                if used_lives == 0:
                    game_over = True
                    print(f'You lose 🤦‍. The hidden word was "{chosen_word}"️. \n')
                    print(draw.hangman_stages[used_lives])

            if "_" not in blank_letters:
                game_over = True
                print(f'You find the word "{chosen_word}" 🏆🏆!')

        except KeyboardInterrupt:
            print("\nHello User, you interrupted the program. Please run me again.")
            sys.exit(0)
        except EOFError:
            print("\nHello User, it is EOF exception, please run me again.")
            sys.exit(0)


hangman()
