
rows = int(input("Rows : "))
cols = 1
count = 1

for x in range(rows):

    for y in range(cols):
        print(count, end="")
        count += 1

    count = 1
    cols += 1
    print("")

# ANSWER

# rows = 5

# 1
# 12
# 123
# 1234
# 12345
