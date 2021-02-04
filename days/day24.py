with open("inputs/input24.txt", "r") as f:
    paths = f.read().splitlines()


def parse_path(p):
    parsed = []
    p_lst = list(p)
    while len(p_lst) != 0:
        char_1 = p_lst.pop(0)
        if char_1 in "ns":
            char_2 = p_lst.pop(0)
            parsed.append(char_1 + char_2)
        else:
            parsed.append(char_1)
    return parsed


def to_cartesian(p):
    n = 0
    e = 0

    for move in p:
        if move == "e":
            e += 2
        elif move == "w":
            e -= 2
        else:
            if "n" in move:
                n += 1
            else:
                n -= 1

            if "e" in move:
                e += 1
            else:
                e -= 1

    return (n, e)


def neighbor_coords(coord):
    (n, e) = coord
    ns = [
        (n, e + 2),
        (n, e - 2),
        (n + 1, e + 1),
        (n - 1, e + 1),
        (n + 1, e - 1),
        (n - 1, e - 1),
    ]
    return ns


def count_blacks(coords, black_tiles):
    count = 0
    for c in coords:
        if c in black_tiles:
            count += 1
    return count


def all_possible(black_tiles):
    total_set = set()
    for t in black_tiles:
        ns = neighbor_coords(t)
        for n in ns:
            total_set.add(n)
        total_set.add(t)
    return total_set


cartesians = [to_cartesian(parse_path(p)) for p in paths]
black_tiles = set()

for c in cartesians:
    if c in black_tiles:
        black_tiles.remove(c)
    else:
        black_tiles.add(c)

print(f"Part 1: {len(black_tiles)}")

for i in range(100):
    new_blacks = set()
    for t in all_possible(black_tiles):
        n = count_blacks(neighbor_coords(t), black_tiles)
        if t in black_tiles:
            if not (n == 0 or n > 2):
                new_blacks.add(t)
        else:
            if n == 2:
                new_blacks.add(t)
    black_tiles = new_blacks

print(f"Part 2: {len(black_tiles)}")
