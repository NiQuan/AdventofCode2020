import re

with open("inputs/input2.txt", "r") as f:
    lines = f.read().splitlines()

count = 0

for line in lines:
    r = re.search("(\d+)-(\d+) (\w): (\w+)", line).groups()
    lower_pos = int(r[0])
    upper_pos = int(r[1])
    c = r[2]
    password = r[3]

    if (password[lower_pos - 1] == c) != (password[upper_pos - 1] == c):
        print(line)
        count = count + 1


print("Count: " + str(count))