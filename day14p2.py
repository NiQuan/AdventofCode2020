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

memory = {}

def pre_process(raw_address, mask):
    address = ""
    for i in range(len(mask)):
        if mask[i] == "1":
            address += "1"
        elif mask[i] == "0":
            address += raw_address[i]
        else:
            address += "X"
    return address

def find_adds(raw_address, mask):
    if mask:
        address = pre_process(raw_address, mask)
    else:
        address = raw_address

    if "X" in address:
        for i in range(len(address)):
            if address[i] == "X":
                first_part = address[:(i)]
                last_part = address[(i+1):]
                ad1 = find_adds(first_part + "0" + last_part, None)
                ad2 = find_adds(first_part + "1" + last_part, None)
                return  ad1 + ad2
    else:
        return [address]

for i in instructions:
    mask = i[0]
    bin_ad = format(i[1],"036b")
    val = i[2]
    
    write_adds = find_adds(bin_ad, mask)

    for a in write_adds:
        memory[a] = val

print(sum([x[1] for x in memory.items()]))
