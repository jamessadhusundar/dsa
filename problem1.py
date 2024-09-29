

input = int(input("Input : "))

count500 = 0
count100 = 0
count50 = 0
count20 = 0
count10 = 0
count5 = 0
count1 = 0

while input >= 500:
    input -= 500
    count500 += 1

while input >= 100:
    input -= 100
    count100 += 1

while input >= 50:
    input -= 50
    count50 += 1

while input >= 10:
    input -= 10
    count10 += 1

while input >= 5:
    input -= 5
    count5 += 1

while input >= 1:
    input -= 1
    count1 += 1

print(f"\nCURRENCY COUNT\n")
print(f"500 : {count500}")
print(f"100 : {count100}")
print(f"50 : {count50}")
print(f"10 : {count10}")
print(f"5 : {count5}")
print(f"1 : {count1}")
