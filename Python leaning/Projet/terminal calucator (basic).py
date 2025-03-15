import time

while True:
    operation = int(input("what operation do you want to do?\n 1. Addition\n 2. Soustraction\n 3. multiplication\n 4. division\n 5. You can also quit by hitting 5\n"))

    if operation in [1, 2, 3, 4]:  
        First_number = float(input("number one: "))
        Second_number = float(input("number two: "))
    
    elif operation == 5:
        print("\nsad you are leaving the GREATEST calucator")
        break
    else:
        print("\nPlease select a valid operation (1, 2, 3, 4 or 5).\n") 

    if operation == 1: 
        result = First_number + Second_number
        print(f"\nit add to {result}\n\n")

    elif operation == 2:
        result = First_number - Second_number
        print(f"\nthe result is {result}\n\n")

    elif operation == 3:
        result = First_number * Second_number
        print(f"\nthe result is {result}\n\n")

    elif operation == 4:
        if Second_number != 0:
            result = First_number / Second_number
            print(f"\nthe result is {result}\n\n")
        else:
            print("Error: Cannot divide by zero.\n")

    time.sleep(4)
    