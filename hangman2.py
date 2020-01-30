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
random_ele_pos = random.sample(range(len(pick)), k = 3)
print(random_ele_pos)
display = ''.join('*' if pos in random_ele_pos else letter for pos, letter in enumerate(pick))

def hangman(count, display, word):
    limit = 3

    guess = input("This is word: " + display + " Enter your guess: ")
    #remains need to handle reapeting characters
    remains = ''.join(word[pos] if letter is '*' else '_' for pos, letter in enumerate(list(display)))
    if guess in remains:
        index = remains.find(guess)
        #word = word[:index] + "*" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display)
    else:
        count += 1
        if count == 1:
            print("Wrong input. " + str(limit - count) + " guess remaining ")
            print(
                 " __ \n"
                 " |      \n"
                 " |      \n"
                 " |      \n"
                 " |      \n"
                 " |      \n"
                 " |      \n"
                 "|_\n"

             )

        elif count == 2:
            print("Wrong input. " + str(limit - count) + " guess remaining ")
            print(
                 " __ \n"
                 " |    | \n"
                 " |    | \n"
                 " |    0 \n"
                 " |      \n"
                 " |      \n"
                 " |      \n"
                 "|_\n"

             )

        elif count == 3:
            print(" Wrong input. You are hanged! ")
            print("   __   \n"
                  "  |   |   \n"
                  "  |   |   \n"
                  "  |   0   \n"
                  "  |  /|\  \n"
                  "  |  / \  \n"
                  "  |       \n"
                  " |_\n"

                  )
    print(display)
    if word == display:
         print("Congrats! You have guessed it successfully.....")
    elif count != limit:
         hangman(count, display, word)

hangman(count, display, word)
