
numbers=[1, 2, 3, 4, 4]

output = list()
original_count = 0
duplicate_count = 0

if len(numbers) > 0:
    output = [numbers[0]]
    original_count= 1

for i in range(1, len(numbers)):
    if numbers[i] != numbers[i - 1]:
        output.append(numbers[i])
        original_count += 1

    else:
        duplicate_count += 1

while duplicate_count > 0:
    output.append("_")
    duplicate_count -= 1

print(original_count, output)