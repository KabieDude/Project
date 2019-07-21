import random

shit_number = random.randint(0, 11)

def fuck(u):

    for x in range(0, 6):
        dec = input("Guess what number I'm thinking.")

        if int(dec) == u:
            print("Correct! :)")
            break

        if int(dec) != u:
            print("Try again. :(")

        if int(dec) > u:
            print("The number is lower.")

        if int(dec) < u:
            print("The number is higher.")

fuck(shit_number)





