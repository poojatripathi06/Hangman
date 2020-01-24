import random
import time

secret_word = 'hey you secret python cat bat rat white black blue heaven hell selena jhon hugh joaquin pooja tripathi '.split()
word = random.choice(secret_word)
length = len(word)
name = input("what is your name: ")
print("Welcome " + name + " Best of luck!....")
time.sleep(1)
print("Test begins now.....")
time.sleep(1)

count = 0
pick = list(word)
show_letters = ['a', 'o', 'e', 'i', 'u']
display = ''.join(letter if letter in show_letters else '*' for letter in pick)

def hangman(count, display, word):
    limit = 3

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
                 " |    | \n"
                 " |    0 \n"
                 " |      \n"
                 " |      \n"
                 " |      \n" 
                 "_|__\n"

             )

        elif count == 3:
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