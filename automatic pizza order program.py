print("Thanks for choosing Python Pizza Deliveries!")
print("Our Pizza sizes prices are:\n Small Pizza (S): $15 \n Medium Pizza (M): $20 \n Large Pizza (L): $25")

pizza_bill = 0

# Get pizza size
size = input("Enter the size of the Pizza: Type 'S' for small, 'M' for medium, and 'L' for large: ").upper()
if size == "S":
    pizza_bill += 15
elif size == "M":
    pizza_bill += 20
elif size == "L":
    pizza_bill += 25
else:
    print("Invalid size! Please restart the order.")
    exit()

# Ask about adding pepperoni
print("We also offer pepperoni as an add-on.\nPepperoni prices are:\n Small Pizza: +$2 \n Medium and Large Pizza: +$3")
add_pepperoni = input("Do you want to add pepperoni to your pizza? (Y or N): ").upper()

if add_pepperoni == "Y":
    if size == "S":
        pizza_bill += 2
    else:
        pizza_bill += 3
elif add_pepperoni != "N":
    print("Invalid input! Please restart the order.")
    exit()

# Ask about adding extra cheese
print("We also offer extra cheese for an additional $1.")
extra_cheese = input("Do you want to add extra cheese to your pizza? (Y or N): ").upper()

if extra_cheese == "Y":
    pizza_bill += 1
elif extra_cheese != "N":
    print("Invalid input! Please restart the order.")
    exit()

# Final bill
print(f"Your final bill is: ${pizza_bill}")
