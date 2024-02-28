import random, sys

hangman_stages = ['''
  ============''', '''
    |            
    |            
    |           
    |           
  ============''', '''
    +-------------
    |            
    |            
    |           
    |           
  ============''', '''
    +-------------
    |            |
    |            
    |           
    |           
  ============''', '''
    +-------------
    |            |
    |            @
    |           
    |           
  ============''', '''
    +-------------
    |            |
    |            @
    |            |
    |           
  ============''', '''
    +-------------
    |            |
    |            @
    |           /|
    |           
  ============''', '''
    +-------------
    |            |
    |            @
    |           /|\\
    |           
  ============''', '''
    +-------------
    |            |
    |            @
    |           /|\\
    |           / 
  ============''', '''
    +-------------
    |            |
    |            @
    |           /|\\
    |           / \\
  ============''']

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
    used_life = 0
    while "_" in blank_list:
        # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
        try:
            guess = input("Guess a letter: ").lower()

            # Check if guess is one of the letters in the chosen_word.
            if guess in chosen_word:
                for i in range(len(chosen_word)):
                    if chosen_word[i] == guess:
                        blank_list[i] = guess
                print(final_blank_letters.join(blank_list), "\n")
            else:
                # Track the count of lives used
                if used_life < 9:
                    print(hangman_stages[used_life])
                    used_life += 1
                else:
                    print(hangman_stages[used_life])
                    print(f"YOU LOSE 🤦‍. The hidden word was '{chosen_word}'️. \n")

        except KeyboardInterrupt:
            print("\nHello User, you interrupted the program. Please run me again.")
            sys.exit(0)
        except EOFError:
            print("\nHello User, it is EOF exception, please run me again.")
            sys.exit(0)

    print("YOU WON 🏆🏆!")


hangman()
