import math
import time
from sympy import symbols, solve, sqrt, cbrt

x, y, z = symbols('x y z')  # Define variables

while True:
    action = int(input("\nwelcome, please select what do you want to do\n\n0. leave\n1. free calculing\n2. calculate Areas\n3. look up formulas\n4. Algebra calculing\nADD MORE FUNCTION (LATER)\n"))
    #free calculing, no formule

    if action == 0:
        print("goodbye...")
        time.sleep(1)
        break

    elif action == 1:
        while True:
            free = input("\nenter you're expression or go back by typing 0\n")

            if free == "0":
                time.sleep(1)
                break

            if free != 0:
                try:
                    result = eval(free)
                    print(f"result: {result:.2f}\n")
                    time.sleep(1)
        
                except Exception as e:
                    print("Error:", e)


    #to calculate areas
    elif action == 2:
        while True:
            area_type = int(input("what shape's area do you want?\n\n0. go back\n1. circle's circonference (Its not an area, I know)\n2. circle's area\n3. cube's volume\n4. cube's area\n"))

            if area_type == 0:
                print("going back...")
                time.sleep(1)
                break

            
            if area_type == 1:
                radius = float(input("\nenter the radius\n"))
                circonference = 2 * math.pi * radius
                print(f"the Circonference is {circonference:.2f}\n")


            elif area_type == 2:
                radius = float(input("\nenter the radius\n"))
                area_circle = math.pi * radius ** 2
                print(f"the area is {area_circle:.2f}")


            elif area_type == 3:
                side = float(input("enter the lenght of the side\n"))
                volume_cube = side ** 3
                print(f"volume: {volume_cube:.2f}")


            elif area_type == 4:
                side = float(input("enter the lenght of the side\n"))
                area_cube = 6 * side ** 2
                print(f"volume: {area_cube:.2f}")

            time.sleep(1)

    #to look up formula
    elif action == 3:
        while True:
            formuhelp = int(input("\nwhat formula do you want?\n\n0. go back\n1. circonference of circle\n2. area of circle\n3. add more\n"))

            if formuhelp == 0:
                print("\ngoind back...")
                time.sleep(1)
                break

            elif formuhelp == 1:
                print("\nthe formula is: C = 2𝝅r\n")

            elif formuhelp == 2:
                print("\nThe formula is: 𝝅r²")

            time.sleep(1)

    #to use algebra
    elif action == 4:
        while True:
            print("\nkill me its not working...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            break


    else:
        print("please type a number from 1 to 4\n\n")