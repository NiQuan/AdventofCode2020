with open("inputs/input1.txt", "r") as f:
    lines = list(map(int, f.read().splitlines()))

# Part 1
for i in range(0, len(lines)):
    for j in range(i, len(lines)):
        if (lines[i] + lines[j]) == 2020:
            print(i * j)

# Part 2
for i in range(0, len(lines)):
    for j in range(i, len(lines)):
        for k in range(j, len(lines)):
            if (lines[i] + lines[j] + lines[k]) == 2020:
                print(i * j * k)

        