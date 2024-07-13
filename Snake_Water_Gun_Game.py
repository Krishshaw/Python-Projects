import random
l=['s','w','g']

chance=10
n=0
comp_point=0
My_point=0
print("\n")
print("\t\t\t Snake ,Water,Gun Game\n \n")
print("s for snake \nw for water \ng for gun \n")

while n< chance:
    i=input('Snake,Water,Gun:')
    r=random.choice(l)

    if i==r:
        print("Tie both 0 point to each\n")

    elif i=="s" and r=="g":
        comp_point=comp_point+1
        print(f"Your guess is {i} and Computer guess is {r}\n")
        print("Computer wins 1 point \n")
        print(f"Computer point is {comp_point} and Your point is {My_point}\n")
    
    elif i=="s" and r=="w":
        My_point=My_point+1
        print(f"Your guess is {i} and Computer guess is {r}\n")
        print("You wins 1 point \n")
        print(f"Computer point is {comp_point} and Your point is {My_point}\n") 
    
    elif i=="w" and r=="s":
        comp_point=comp_point+1
        print(f"Your guess is {i} and Computer guess is {r}\n")
        print("Computer wins 1 point \n")
        print(f"Computer point is {comp_point} and Your point is {My_point}\n")

    elif i=="w" and r=="g":
        My_point=My_point+1
        print(f"Your guess is {i} and Computer guess is {r}\n")
        print("You wins 1 point \n")
        print(f"Computer point is {comp_point} and Your point is {My_point}\n") 

    elif i=="g" and r=="s":
        comp_point=comp_point+1
        print(f"Your guess is {i} and Computer guess is {r}\n")
        print("Computer wins 1 point \n")
        print(f"Computer point is {comp_point} and Your point is {My_point}\n")

    elif i=="g" and r=="w":
        My_point=My_point+1
        print(f"Your guess is {i} and Computer guess is {r}\n")
        print("You wins 1 point \n")
        print(f"Computer point is {comp_point} and Your point is {My_point}\n") 

    else:
        print("Wromg Input\n")

    n=n+1
    print(f"{chance-n} is left out of {chance} \n")

print("Game Over!!!\n")

if comp_point==My_point:
    print("Tie\n")

elif comp_point>My_point:
    print("Computer Wins\n")

else:
    print("You Wins\n")


