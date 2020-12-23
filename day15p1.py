with open("inputs/input15.txt", "r") as f:
    start_nums = [int(c) for c in f.read().split(',')]

history = start_nums
start = len(start_nums)

for i in range(start, 2020):
    recent = history[-1]
    if recent in history[:-1]:
        last_used = len(history) - history[-2::-1].index(recent) - 2
        history += [(i-1) - last_used]
    else:
        history += [0]

print(history[-1])
