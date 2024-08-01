#A SIMPLE ROLLERCOASTER FARE CALCULATOR WITH AN ADDITIONAL PHOTO TAKING ADDON IN THE BILL
#USING IF ELSE AND ELIF
height = int(input("Enter your height in cm.. "))
age = int(input("Enter your age..."))
bill=0
if height >= 120:
    if age >= 18:
        bill = bill +12
        print("your ticket price is $12")
    elif age >=12 and age<18:
        bill = bill +7
        print("your ticket price is $7 ")
    else:
        bill = bill +5
        print("your ticket price is $5")
    want_photo = input("Do you want photo taken? Press Y for yes and N for no ")
    if want_photo == "y" :
        bill = bill +3
        print("The price of this addon is $3")

    elif want_photo == "n":
        print("Okay this addon will not add to your bill")
        
print("Your total payable amount is ",bill)

