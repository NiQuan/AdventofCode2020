with open("inputs/input10.txt", "r") as f:
    joltages = [0] + [int(n) for n in f.read().splitlines()] #Adding the 0 for the source

joltages.sort()
joltage_gaps = [joltages[i+1] - joltages[i] for i in range(len(joltages) - 1)]
num_1s = len(list(filter(lambda x : x == 1, joltage_gaps)))
num_3s = len(list(filter(lambda x : x == 3, joltage_gaps))) + 1 #Add one for the 3 jolt gap to the desination

print(num_1s * num_3s)
