import random

word_list = ["aardvark", "baboon", "camel"]
blank_letters = ""

# Randomly choose a word from the word_list
chosen_word = random.choice(word_list)
print("chosen word is:", chosen_word)

# Generate blank letters for chosen_word
for letter in chosen_word:
    blank_letters += "_"
print(blank_letters)

# Transform string in a list
blank_list = list(blank_letters)
final_blank_letters = ""


def hangman():
    while "_" in blank_list:
        # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
        guess = input("Guess a letter: ").lower()

        # Check if guess is one of the letters in the chosen_word.
        if guess in chosen_word:
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    blank_list[i] = guess
                    print(final_blank_letters.join(blank_list), "\n")
    print("YOU WON 🏆🏆", final_blank_letters)


hangman()
