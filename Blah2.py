def decision(direction):

    if direction == "S" or direction == "s":
        print("You have moved south. ")

    if direction == "W" or direction == "w":
        print("You have moved west. ")

    if direction == "N" or direction == "n":
        print("You Have moved north. ")

    if direction == "E" or direction == "e":
        print("You have moved east. ")

dec = (input("blah blah blah (you can move 'N,E,S,W.') "))


decision(dec)


def North2(direction_2):

    if direction_2 == "N" or direction_2 == "n":
        print("dead end go back" )
        

    if direction_2 == "E" or direction_2 == "e":
        print("You exited the room and are greeted by a dark hallway. ")


dec_2 = (input("Please press 'N or E' to move. "))

North2(dec_2)



