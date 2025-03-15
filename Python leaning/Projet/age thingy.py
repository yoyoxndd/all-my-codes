import time

while True:

    try:
        age = int(input("what is your age?\n"))

        time.sleep(.5)

        age2 = input(f"Are you {age} years old?\nYes or no\n").lower()
        
        time.sleep(.5)
        
        if age2 == "no":
            print("please re-type your age")
            continue

        if 1 <= age <= 17:
            print("You are too young to use our services")
            break

        elif 17 < age:
            print("lets continue.")
            break

        else:
            print("please write a positive number.")
    
    except ValueError:
        print("please type a valid number")
