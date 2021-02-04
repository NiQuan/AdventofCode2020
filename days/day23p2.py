circle_size = 1000000
starting_cups = [int(x) for x in list("562893147")] + list(range(10, circle_size + 1))

max_val = max(starting_cups)
last = starting_cups[0]
starting_cups = starting_cups[1:]
first = last
cups = {}
for i in starting_cups:
    cups[last] = i
    last = i
cups[i] = first  # Complete the loop


def cups_to_str(c):
    last = 1
    result = ""
    count = 0
    while True:
        result += str(last)
        last = c[last]
        count += 1
        if last == 1:
            break
        if count == 15:
            result += "..."
            break
    return result


current = first

for i in range(10000000):
    three_pulled = []
    p2 = cups[current]
    for j in range(3):
        three_pulled.append(p2)
        p2 = cups[p2]

    cups[current] = p2

    found = False
    j = current - 1
    while not found:
        if j <= 0:
            j = max_val

        if not (j in three_pulled):
            dest = j
            found = True

        j -= 1
    dest_next = cups[dest]
    cups[dest] = three_pulled[0]
    cups[three_pulled[0]] = three_pulled[1]
    cups[three_pulled[1]] = three_pulled[2]
    cups[three_pulled[2]] = dest_next

    current = cups[current]


star_1 = cups[1]
star_2 = cups[star_1]

print(f"Result: {star_1 * star_2}")
