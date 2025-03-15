#1 not really practicle
color = input("what is your favorite color?\n")
print("my favorite color is: ", color)
#1,5 THE F STRING MAKE IT EASIER
name = input("what is your name?\n")
print(f"Welcome, {name}")


#2
my_name = "bob"
print(f"Hello and welcome {my_name}")


#3
color = input("what is your favorite color ?\n 1. blue\n 2. BLACK\n 3. WhItE\n 4. yellew\n")

try:
    color = int(color)

except ValueError:
    print("YOU DONT HAVE THAT MUCH CHOICE!!!")
    color=None

if color == 1:
    print("ur basic")
elif color == 2:
    print("it aint a color")
elif color == 3:
    print("it aint a color?")
elif color == 4:
    print("ewww")
elif color is not None:
    print("come back when you choose")


#4
ef
