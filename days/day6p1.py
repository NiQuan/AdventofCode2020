letters = "abcdefghijklmnopqrstuvwxyz"

with open("inputs/input6.txt", "r") as f:
    groups = f.read().split("\n\n")

total = 0

for group in groups:
    num = len([c for c in letters if c in group])
    total += num

print(total)