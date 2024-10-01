
input = [1, 2, 3, 4, 5]

smallest = largest = input[0]

for i in input:

    # SMALLEST
    if i < smallest:
        smallest = i

    # LARGEST
    if i > largest:
        largest = i

second_smallest = largest
second_largest = smallest

for i in input:

    # SECOND SMALLEST
    if i < second_smallest and i > smallest:
        second_smallest = i

    # SECOND LARGEST
    if i > second_largest and i < largest:
        second_largest = i

print(f"Smallest : {smallest}")
print(f"Second smallest : {second_smallest}")
print(f"Largest : {largest}")
print(f"Second largest : {second_largest}")