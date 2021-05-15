"""Write a program for a matchstick game being played between
the computer and a user. Your program should ensure that the
computer always wins. Rules for the game are as follows:
− There are 21 matchsticks.
− The computer asks the player to pick 1, 2, 3, or 4
matchsticks.
− After the person picks, the computer does its
picking.
− Whoever is forced to pick up the last matchstick
loses the game. """

matchstick = 21 
while matchstick > 1:
    user = int(input("user's turn : "))
    matchstick = matchstick - user
    print("Remaning matchstics " + str(matchstick))
    computer = 5 - user
    print("computer's turn " + str(computer))
    matchstick = matchstick - computer
    print("Remaning matchstics "+ str(matchstick))
print("computer wins")