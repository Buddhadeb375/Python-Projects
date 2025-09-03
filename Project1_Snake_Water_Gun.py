#Snake Water Gun
import random
"""
1 for snake, -1 for water, 0 for gun
"""
i=0# For computer
j=0# for Person
print("Welcome to Snake Water Gun Game!!")
print("In this game the first player to win 3 Games win")
print("s for snake, w for water, g for gun")
while(i<3 and j<3):
    yourchoice=input("Enter Your choice: ")
    computerchoice=random.choice([-1,0,1])
    yourDict={"s":1,"w":-1,"g":0}
    reverseDict={1:"Snake",-1:"Water",0:"Gun"}
    you=yourDict[yourchoice.lower()]
    print(f"You chose {reverseDict[you]} & Computer chose {reverseDict[computerchoice]}")
    if(computerchoice==you):
        print("It's a Draw")
    else:
        if(computerchoice==-1 and you==1):
            j+=1
            print(f"You:{j} Computer:{i}")
        elif(computerchoice==-1 and you==0):
            i+=1
            print(f"You:{j} Computer:{i}")
        elif(computerchoice==1 and you==-1):
            j+=1
            print(f"You:{j} Computer:{i}")
        elif(computerchoice==1 and you==0):
            i+=1
            print(f"You:{j} Computer:{i}")
        elif(computerchoice==0 and you==-1):
            j+=1
            print(f"You:{j} Computer:{i}")
        elif(computerchoice==0 and you==1):
            i+=1
            print(f"You:{j} Computer:{i}")
        else:
            print("Please enter write choice")
if(j==3):
    print("You Win!!")
elif(i==3):
    print("Computer Win!!")