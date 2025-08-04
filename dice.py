import random

while True:
    user_message= input("Roll the dice? (y/n)").strip(). lower()
    
    if user_message != "y" and user_message !="n":
        print("Invalid choice!")
    elif user_message== "y":
        choice1= random.randint(1, 6)
        choice2= random.randint(1, 6)
        print(f"({choice1}, {choice2})")
    elif user_message== "n":
        print("Thanks for playing!")
        break

