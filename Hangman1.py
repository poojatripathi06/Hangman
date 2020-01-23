import random
import time

secret_word = ["hey", "rio", "ola"]
word = random.choice(secret_word)
length = len(word)
name = input("what is your name: ")
print("Welcome " + name + " Best of luck!....")
time.sleep(2)
print("Test begins now.....")
time.sleep(2)

count = 0
display = '*' * length

def hangman(count, display, word):
    limit = 6

    guess = input("This is word: " + display + " Enter your guess: ")
    if guess in word:
        index = word.find(guess)
        word = word[:index] + "*" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display)
    else:
        count += 1
        if count == 1:
            print("Wrong input. " + str(limit - count) + " guess remaining ")
            print(
                 " ______ \n"
                 " |      \n"
                 " |      \n"
                 " |      \n"
                 " |      \n"
                 " |      \n"
                 " |      \n" 
                 "_|__\n"

             )

        elif count == 2:
            print("Wrong input. " + str(limit - count) + " guess remaining ")
            print(
                 " ______ \n"
                 " |    | \n"
                 " |      \n"
                 " |      \n"
                 " |      \n"
                 " |      \n"
                 " |      \n" 
                 "_|__\n"

             )
        elif count == 3:
            print(" Wrong input. " + str(limit - count) + " guess remaining ")
            print(" ____ \n"
                  " |   | \n"
                  " |   | \n"
                  " |     \n"
                  " |     \n"
                  " |     \n"
                  " |     \n"
                  "_|__\n"

                  )
        elif count == 4:
            print(" Wrong input. " + str(limit - count) + " guess remaining ")
            print(" ____ \n"
                  " |   | \n"
                  " |   | \n"
                  " |   0  \n"
                  " |     \n"
                  " |     \n"
                  " |     \n"
                  "_|__\n"

                  )
        elif count == 5:
            print(" Wrong input. " + str(limit - count) + " guess remaining ")
            print(" ____   \n"
                  " |   |  \n"
                  " |   |  \n"
                  " |   0  \n"
                  " |  /|\ \n"
                  " |      \n"
                  " |      \n"
                  "_|__\n"

                  )
        elif count == 6:
            print(" Wrong input. You are hanged! ")
            print("   ____   \n"
                  "  |   |   \n"
                  "  |   |   \n"
                  "  |   0   \n"
                  "  |  /|\  \n"
                  "  |  / \  \n"
                  "  |       \n"
                  " _|__\n"

                  )
    if word == '*' * length:
         print("Congrats! You have guessed it successfully.....")
    elif count != limit:
         hangman(count, display, word)

hangman(count, display, word)