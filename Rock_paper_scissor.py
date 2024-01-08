import random
my_choice=int(input("Enter your choice: Press 0 for Rock\nPress 1 for paper\nPress 2 for scissor\n"))
if my_choice >=3 or my_choice <0:
    print("You have entered invalid number\nYou lose!")
else:
    system_choice=random.randint(0,2)
    print("sytem's choice is as")
    print(system_choice)
    if  system_choice == my_choice:
        print("Game is draw")
    elif system_choice == 0 and my_choice == 2:
        print("You lose!")
    elif  my_choice == 0 and system_choice == 2:
        print("Congrates! You win")
    elif system_choice > my_choice:
        print("You lose!")
    elif my_choice > system_choice:
        print(" Congrates! You win")

    

