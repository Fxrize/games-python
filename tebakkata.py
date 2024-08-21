import random
# library that we use in order to choose
# on random words from a list of words

name = input("Siapa Namamu? ")

# Here the user is asked to enter the name first

print("Semoga Beruntung ! ", name)

words = ['sekolah', 'komputer', 'coding', 'programming',
         'matematika', 'belajar', 'pemain', 'tidur',
         'mancing', 'tanah', 'air', 'kucing']

# Function will choose one random
# word from this list of words
word = random.choice(words)


print("Tebak kata")

guesses = ''

# any number of turns can be used here
turns = 12


while turns > 0:

    # counts the number of times a user fails
    failed = 0

    # all characters from the input
    # word taking one at a time.
    for char in word:

        # comparing that character with
        # the character in guesses
        if char in guesses:
            print(char, end=" ")

        else:
            print("_")

            # for every failure 1 will be
            # incremented in failure
            failed += 1

    if failed == 0:
        # user will win the game if failure is 0
        # and 'You Win' will be given as output
        print("Kamu Menang!")

        # this print the correct word
        print("Kata tersebut adalah : ", word)
        break

    # if user has input the wrong alphabet then
    # it will ask user to enter another alphabet
    print()
    guess = input("Tebak kata :")

    # every input character will be stored in guesses
    guesses += guess

    # check input with the character in word
    if guess not in word:

        turns -= 1

        # if the character doesn’t match the word
        # then “Wrong” will be given as output
        print("Salah")

        # this will print the number of
        # turns left for the user
        print("Kamu mempunyai", + turns, 'kesempatan')

        if turns == 0:
            print("Kamu Kalah!")
