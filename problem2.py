# PROBLEM - 1

# A World cinema wants to implement a ticket pricing system that automatically calculates the ticket
# price based on a customer's age. The cinema has set different price categories for different age groups
# to ensure affordability for children and seniors, while maintaining regular prices for adults and
# teenagers. In the world of entertainment, ticket prices vary based on age. Your task is to create a
# program that calculates the ticket price for a movie based on the age of the viewer.
# • Children (age 0-12): 10
# • Teenagers (age 13-19): 15
# • Adults (age 20-60): 20
# • Seniors (age 61 and above): 12

print("Hello!")

age = int(input("Enter your age : "))

if age >= 1 and age <= 12:
    print("You are a child.")
    print("Pay 10/-")

elif age >= 13 and age <= 19:
    print("You are a teenager.")
    print("Pay 15/-")

elif age >= 20 and age <= 60:
    print("You are an adult.")
    print("Pay 20/-")

elif age > 60:
    print("You are a senior citizen.")
    print("Pay 18/-")

else:
    print("Invalid age.")

# PROBLEM - 2

# You run a retail store and want to implement a discount system to attract more customers. You've decided to
# offer different discount rates based on the purchase amount to incentivize customers to spend more. This will
# not only increase sales but also reward loyal customers with greater discounts. Craft a program that calculates
# the discount amount based on the purchase amount. Apply different discount rates for different purchase
# ranges and display the calculated discount amount.
# Conditions:
# • If the purchase amount is less than or equal to 1000, no discount is applied.
# • For amounts between 1000 and 2000, apply a 10% discount.
# • For amounts between 2000 and 5000, apply a 15% discount.
# • For amounts greater than 5000, apply a 20% discount

print("Hello!")

purchase_amount = int(input("Enter the total bill amount : "))

if purchase_amount <= 1000:
    print(f"Total bill amount : {purchase_amount}/-")
    print("No discount")

elif purchase_amount > 1000 and purchase_amount <= 2000:
    print(f"Bill amount : {purchase_amount}/-")
    print("Discount : 10%")
    print(f"Total bill amount : {purchase_amount - (purchase_amount * (10 / 100))}/-")

elif purchase_amount > 2000 and purchase_amount <= 5000:
    print(f"Bill amount : {purchase_amount}/-")
    print("Discount : 15%")
    print(f"Total bill amount : {purchase_amount - (purchase_amount * (15 / 100))}/-")

elif purchase_amount > 5000:
    print(f"Bill amount : {purchase_amount}/-")
    print("Discount : 20%")
    print(f"Total bill amount : {purchase_amount - (purchase_amount * (20 / 100))}/-")

else:
    print("Invalid bill amount.")