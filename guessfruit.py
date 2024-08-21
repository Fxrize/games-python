# Python Program to illustrate
# Hangman Game
import random
from collections import Counter

someWords = '''apel mangga jeruk durian nanas anggur pisang manggis melon semangka salak rambutan jambu sawo kiwi'''

someWords = someWords.split(' ')
# randomly choose a secret word from our "someWords" LIST.
word = random.choice(someWords)

if __name__ == '__main__':
    print('Tebak kata! HINT : nama buah-buahan ')

    for i in word:
        # For printing the empty spaces for letters of the word
        print('_', end=' ')
    print()

    playing = True
    # List for storing the letters guessed by the player
    letterGuessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0
    try:
        while (chances != 0) and flag == 0:  # Flag is updated when the word is correctly guessed
            print()
            chances -= 1

            try:
                guess = str(input('Masukkan huruf : '))
            except:
                print('Hanya bisa huruf!')
                continue

            # Validation of the guess
            if not guess.isalpha():
                print('Hanya bisa huruf!')
                continue
            elif len(guess) > 1:
                print('Hanya bisa satu huruf')
                continue
            elif guess in letterGuessed:
                print('Kamu sudah menggunakan huruf ini')
                continue

            # If letter is guessed correctly
            if guess in word:
                # k stores the number of times the guessed letter occurs in the word
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess  # The guessed letter is added as many times as it occurs

            # Print the word
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char, end=' ')
                    correct += 1
                # If user has guessed all the letters
                # Once the correct word is guessed fully,
                elif (Counter(letterGuessed) == Counter(word)):
                    # the game ends, even if chances remain
                    print("Kata tersebut adalah : ", end=' ')
                    print(word)
                    flag = 1
                    print('Selamat,Kamu Menang!')
                    break  # To break out of the for loop
                    break  # To break out of the while loop
                else:
                    print('_', end=' ')

        # If user has used all of his chances
        if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print('Game Over! :( ')
            print('Kata tersebut adalah {}'.format(word))

    except KeyboardInterrupt:
        print()
        print('Bye! Coba lagi.')
        exit()
