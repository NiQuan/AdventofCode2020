letters = "abcdefghijklmnopqrstuvwxyz"

with open("inputs/input6.txt", "r") as f:
    groups = f.read().split("\n\n")

total = 0

for group in groups:
    people = group.split()
    for c in letters:
        if all(c in p for p in people):
            total += 1

print(total)