import random
"""
1 is for snake
-1 is for  water
0 for gun
"""

computer = random.choice([-1,0,1])
youstr = input("Enter your choice :  ")
yourDict = {"s" : 1 , "w" : -1 , "g" : 0}
reversedict = {1 : "s" , -1 : "w" , 0 : "g" }


you = yourDict[youstr]
print("your choice is " + reversedict[you])
print("computer choice is " + reversedict[computer])

if(computer ==  -1 and you == 1):
    print("You win")

elif(computer ==  1 and you == -1):
    print("You lose")

elif(computer ==  0 and you == -1):
    print("You win")

elif(computer ==  0 and you == 1):
    print("You lose")

elif(computer ==  1 and you == 0):
    print("You win")

elif(computer ==  -1 and you == 0):
    print("You lose")

else:
    print("Draw")




