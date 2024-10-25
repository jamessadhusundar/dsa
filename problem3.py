# PROBLEM - 1

# Sarah, a busy professional, finishes her workday and needs to attend an important meeting across town. She
# hails a taxi and travels a distance of 15 kilometres to reach her destination. The taxi driver, using the fare
# calculation system, computes the fare as follows: Since Sarah’s journey is between 10 and 100 kilometres, the
# fare is calculated as follows:
# • $110 for the first 10 kilometres
# • $10 for each additional kilometres beyond the initial 10 kilometres
# So, the total fare for Sarah’s journey is calculated as $110 (for the first 10 kilometres) plus $50 (for the
# additional 5 kilometres at $10 per kilometres), resulting in a total fare of $160.
# The taxi driver displays the fare on the meter, and Sarah pays the amount before exiting the taxi. Write a
# program to calculate the transportation fare based on the kilometres covered. Prompt the user to enter the
# kilometres covered. If the kilometres covered are less than or equal to 10, the fare is $11 per kilometres.
# If the kilometres covered are between 11 and 100 (inclusive), the fare is $10 per kilometres after the first 10
# kilometres. If the kilometres covered are more than 100, the fare is $9 per kilometres after the first 100
# kilometres. Calculate and display the total amount to pay. Display "Invalid" for invalid inputs like
# negative numbers and zero.

print("Hello!")

fare_prize = 0

destination = int(input("Distance of your destination : "))

if destination <= 10:
    fare_prize = destination * 10
    print(f"Taxi fare : {fare_prize}/-")

elif destination > 10 and destination <= 100:
    fare_prize = (destination * 11) - 10
    print(f"Taxi fare : {fare_prize}/-")

else:
    fare_prize = 1090 + ((destination - 100) * 9)
    print(f"Taxi fare : {fare_prize}/-")

# PROBLEM - 2

# In a classic chase scenario, Tom is pursuing Jerry, who has consumed Tom’s favorite food. Jerry runs at a speed
# of X meters per second, while Tom chases at a speed of Y meters per second. The task is to determine whether
# Tom will be able to catch Jerry. It’s important to note that initially, Jerry is not at the same position as Tom. Craft
# a program that takes Jerry’s speed (X), Tom’s speed (Y), and the initial distance between them as input, and
# calculates whether Tom will be able to catch Jerry. Consider the scenario where Jerry starts at a different
# position than Tom. The task is to determine whether Tom, with his speed Y meters per second, will be able to
# catch Jerry, who dashes at X meters per second. You’ll need to calculate the time it takes for Tom to catch Jerry
# based on their speeds and the initial distance between them.

print("Hello!")

time = 0

tom_speed = float(input("Enter Tom's speed (meter/sec): "))

jerry_speed = float(input("Enter Jerry's speed (meter/sec): "))

if tom_speed < jerry_speed:
    print("Tom cannot catch Jerry.")

else:
    gap = float(input("Enter the distance between them (at initial point): "))

    if gap > gap - (tom_speed - jerry_speed):
        print("Tom will catch jerry in less than one second.")

    else:
        while gap >= 0:
            gap -= tom_speed - jerry_speed
            time += 1

        print(f"Tom will catch jerry in {time} seconds.")