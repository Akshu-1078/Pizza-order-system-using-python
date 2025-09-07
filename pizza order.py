print("Welcome to the python Pizza Delivery")
size = input("What size pizza do you want? S,M OR L: ")
pepperoni = input("Do You want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# to do work out how much they need to pay based on their size choice.
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You typed the wrong inputs.")


# to do work out how much they need to pay based on their pepperoni choice.
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# to do work out how much they need to pay based on whether if they want extra cheese.
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")