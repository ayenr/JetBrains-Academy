from random import choice


def play():
    words = ['python', 'java', 'kotlin', 'javascript']

    chosen = choice(words)
    chosen_set = set(chosen)
    hint = ["-"] * len(chosen)
    lives = 8
    guess_list = []

    while lives > 0:

        print()
        print("".join(hint))

        if ("".join(hint)) == chosen:
            print('You survived!')
            break

        guess = input("Input a letter:")

        if len(guess) > 1:
            print('You should input a single letter')
        elif not guess.isalpha() or not guess.islower():
            print('Please enter a lowercase English letter')
        elif guess in guess_list:
            print("You've already guessed this letter")
        elif guess in chosen_set:
            guess_list += guess
            for i in range(len(chosen)):
                if chosen[i] == guess:
                    hint[i] = guess
        elif guess not in chosen:
            guess_list += guess
            lives -= 1
            if lives == 0:
                print("That letter doesn't appear in the word")
                print("You lost!")
            else:
                print("That letter doesn't appear in the word")


def game():

    while True:
        print()
        decide = input('Type "play" to play the game, "exit" to quit')

        if decide == "play":
            play()
        elif decide == 'exit':
            break


print("H A N G M A N")

game()
