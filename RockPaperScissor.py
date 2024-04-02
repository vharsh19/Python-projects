import random
user_dict={
    1:"Rock",
    2 : "Paper",
    3:"Scissor"
}
comp_dict={
    1:"ROCK",
    2:"PAPER",
    3:"SCISSOR"
}
print("Welcome Aboard Player!!!")
print("Rules:\nYou Choose a Number among 1 to 3.\nEach number represents an object.")
print("1-Rock\n2-Paper\n3-Scissor\n")
print("Rock wins against Scissor but loses against Paper")
print("Paper wins against Rock but loses against Scissor")
print("Scissor wins against Paper but loses against Rock\n")
print("TO QUIT PLAYING PRESS 'Q'.")
print("ENJOY!!!!!!!!")
Txt='*'
print(100*Txt)
print ("Let's Start")
user_count=0
comp_count=0
while True:
    user_choice1=(input("Enter your choice: "))
    if(user_choice1=='Q'):
        break
    user_choice=int(user_choice1)
    print("\nWaiting for the computer to choose: ")
    comp_choice1=random.choice([1,2,3],p=[0.29,0.43,0.31])
    comp_choice=int(comp_choice1)
    if(user_choice>0 and user_choice<4):
        if(comp_choice==user_choice):
            comp_choice=random.randint(1,3)#giving a second chance so we get difeerent outcome

        if(comp_choice==user_choice):
            print(user_dict.get(user_choice),"<=>",comp_dict.get(comp_choice),"-----> IT IS A DRAW")

        elif((user_choice==1 and comp_choice==3)or(user_choice==2 and comp_choice==1)or(user_choice==3 and comp_choice==2)):
            print(user_dict.get(user_choice),"<=>",comp_dict.get(comp_choice),"-----> PLAYER WINS")
            user_count+=1
        else:
            print(user_dict.get(user_choice),"<=>",comp_dict.get(comp_choice),"-----> COMPUTER WINS")
            comp_count+=1
    else:
        print("Wrong Choice.Please Try Again.")

print("Final Score:\nPlayer: ",user_count,"\nComputer: ",comp_count)
if(user_count>comp_count):
    print("PLAYER WINS")
elif(comp_count>user_count):
    print("COMPUTER WINS")
else:
    print("IT IS A TIE")
print("\n\n###########  THANK YOU FOR PLAYING  ##########")
