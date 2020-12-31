import re

with open("inputs/input2.txt", "r") as f:
    lines = f.read().splitlines()

count = 0

for line in lines:
    r = re.search("(\d+)-(\d+) (\w): (\w+)", line).groups()
    lower_bound = int(r[0])
    upper_bound = int(r[1])
    c = r[2]
    password = r[3]

    num_matches = password.count(c)
    if lower_bound <= num_matches <= upper_bound:
        print(line)
        count = count + 1


print("Count: " + str(count))