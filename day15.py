with open("inputs/input15.txt", "r") as f:
    start_nums = [int(c) for c in f.read().split(',')]

hist_dict = {}
count = 1
for n in start_nums: # Initialize the history dict
    hist_dict[n] = count
    count += 1

def next_num(d, recent, t):
    last_t = d.get(recent)

    if last_t:
        return t - last_t
    else:
        return 0

start = len(start_nums)
recent = start_nums[-1]

for t in range(start, 30000000):
    n = next_num(hist_dict, recent, t)

    hist_dict[recent] = t
    recent = n

print(n)
