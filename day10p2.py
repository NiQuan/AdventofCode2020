import math

with open("inputs/input10.txt", "r") as f:
    joltages = [0] + [int(n) for n in f.read().splitlines()] #Adding the 0 for the source

joltages.sort()
joltage_gaps = [joltages[i+1] - joltages[i] for i in range(len(joltages) - 1)] + [3]

one_streak_lens = []
one_streak_ct = 0

for gap in joltage_gaps:
    if gap == 1:
        one_streak_ct += 1
    else:
        one_streak_lens += [one_streak_ct]
        one_streak_ct = 0

print(joltages)
print(joltage_gaps)
print(one_streak_lens)

acc = 1
for i in one_streak_lens:
    if 0 < i <= 3:
        acc = acc * (2 ** (i - 1))
    elif i == 4:
        acc = acc * 7
    elif i > 4:
        raise (i)

print(int(acc))
