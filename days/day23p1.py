start = [int(x) for x in list("562893147")]
max_val = max(start)


def rotate_one(lst):
    new = lst[1:] + [lst[0]]
    return new


cups = start

for i in range(100):
    print(f"\n---{i+1}---")
    print(f"0: {cups}")
    current = cups[0]
    three_pulled = cups[1:4]
    cups = [cups[0]] + cups[4:]

    j = current - 1
    found = False
    while not found:
        if (j) in cups:
            destination = cups.index(j)
            print(f"dest value: {j}")
            found = True
        j -= 1
        if j <= 0:
            j = max_val
    # print(f"1: {cups}")
    print(f"Destination: {destination}")
    cups = cups[: destination + 1] + three_pulled + cups[destination + 1 :]
    # print(f"2: {cups}")
    cups = rotate_one(cups)

print(f"Final cups: {cups}")
one_loc = cups.index(1)
p1_lst = cups[(one_loc + 1) :] + cups[:one_loc]
p1_ans = "".join(str(i) for i in p1_lst)

print(p1_ans)