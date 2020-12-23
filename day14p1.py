import re

instructions = []
inst_match = re.compile("mem\[(\d+)\] = (\d+)")

with open("inputs/input14.txt", "r") as f:
    for line in f.read().splitlines():
        if line[:4] == "mask":
            current_mask = line.split()[2]
        else:
            (ad, val) = inst_match.match(line).groups()
            instructions += [(current_mask, int(ad), int(val))]

mem_dict = {}

for i in instructions:
    mask = i[0]
    ad = i[1]
    bin_val = format(i[2],"036b")
    result_str = ""
    for i in range(len(bin_val)):
        if mask[i] == "X":
            result_str += bin_val[i]
        else:
            result_str += mask[i]

    mem_dict[ad] = int(result_str, 2)

print(sum([x[1] for x in mem_dict.items()]))


