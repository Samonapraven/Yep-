import random
winning_number = random.randrange(1, 100)


class hints:
    global hint1

    def hint1():
        if (winning_number % 2) == 0:
            print('The number is even!')
        else:
            print('The number is odd!')

    global hint2

    def hint2():
        if (winning_number > 50):
            print('The number is bigger than 50!')
        else:
            print('The number is smaller than 50!')

    global hint3

    def hint3():
        if (winning_number > 85):
            print('The number is close to 100!')
        else:
            print('The number is not close to 100!')


def hinting():
    take_a_hint = random.randrange(1, 4)
    if take_a_hint == 1:
        hint1()
    elif take_a_hint == 2:
        hint2()
    else:
        hint3()


def playing():
    number_try = int(input('Guess the number:'))
    if number_try == winning_number:
        print('Congratulations! You guessed the number! It was: ', winning_number)
    elif tries < tries:
        print('Game over! You lost bozo')
        quit
    elif (number_try != winning_number):
        print('Wrong number, heres a hint:')
        hinting()
        playing()



def asking():
    global tries
    tries = int(input('Enter how many tries you want:'))
    playing()


def trying():
    global tries
    asking()
    if tries > 100:
        print('Way too many tries!')
        asking()
    else:
        print('Go on:')
        playing()


asking()
