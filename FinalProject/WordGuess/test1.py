import random


LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8            # Initial number of guesses player starts with
word_to_guess = "BEAUTIFUL"
word_to_guess1 = list(word_to_guess)


def main():
    # print(word_to_guess)
    print("The word now looks like this: " + "_" * len(word_to_guess))
    print("You have " + str(INITIAL_GUESSES) + " guesses left")
    count = INITIAL_GUESSES
    success_char = []
    while count > 0:
        user_guess = input("Type a single letter here, then press enter: ")
        user_guess = user_guess.upper()
        listed = ''.join([c if c in success_char else "_" for c in word_to_guess1])
        if len(user_guess) > 1 or user_guess == "":
            print("Guess should only be a single character.")
            print("The word now looks like this: " + str(listed))
            print("You have " + str(count) + " guesses left")
        elif user_guess not in word_to_guess:
            count -= 1
            print("There are no " + str(user_guess) + "'s in the word")
            if count == 0:
                print("Sorry, you lost. The secret word was: " + str(word_to_guess))
            else:
                print("You have " + str(count) + " guesses left")
                print("The word now looks like this: " + str(listed))
        else:
            print("The guess is correct")

            if user_guess not in success_char:
                success_char.append(user_guess)
            listed = ''.join([c if c in success_char else '_' for c in word_to_guess1])
            # print(''.join(success_char[:]))
            if set(success_char[:]) == set(word_to_guess1[:]):
                print("Congratulations, the word is: " + str(word_to_guess))
                break
            print("You have " + str(count) + " guesses left")
            print("The word now looks like this: " + str(listed))


if __name__ == "__main__":
    main()