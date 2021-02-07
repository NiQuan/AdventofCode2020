import numpy as np

with open("inputs/input20.txt", "r") as f:
    lines = f.read()

tiles_raw = [l.splitlines() for l in lines.split("\n\n")]
tiles_raw = [t for t in tiles_raw if t]  # Delete empty

tiles_index = {}
tile_ids = []
edge_counts = {}

for t in tiles_raw:
    id = int(t.pop(0)[-6:-1])
    arr = np.array([list(x) for x in t])
    tiles_index[id] = arr
    tile_ids.append(id)


def possible_edges(t):
    base_edges = [t[0, :], t[-1, :], t[:, 0], t[:, -1]]
    edges = base_edges[:]

    for e in base_edges:
        edges.append(e[::-1])

    return edges


def transpositions(t):
    trans = []
    current = t[:, :]
    for i in range(4):
        trans.append(current)
        trans.append(
            np.fliplr(current)
        )  # These flips and rotations will include some transpositions multiple times
        trans.append(np.flipud(current))
        current = np.rot90(current)

    return trans


def find_match(tile, tile_id, tiles_index, tile_ids, direct):
    t = tile
    if direct == "R":
        match_edge = t[:, -1]
    else:
        match_edge = t[-1, :]

    for i in tile_ids:
        if i == tile_id:
            continue
        for j in transpositions(tiles_index[i]):
            if direct == "R" and (j[:, 0] == match_edge).all():
                return (i, j)
            elif direct != "R" and (j[0, :] == match_edge).all():
                return (i, j)

    return None


def print_stiched(s):
    for i in s:
        for j in i:
            print(j, end="")
        print("")
    print("")


def stich(tile_array):
    def make_row(arr, i):
        row = arr[i][0][1:-1, 1:-1]
        for j in arr[i][1:]:
            row = np.concatenate((row, j[1:-1, 1:-1]), axis=1)
        return row

    stiched = make_row(tile_array, 0)
    for i in range(len(tile_array))[1:]:
        stiched = np.concatenate((stiched, make_row(tile_array, i)), axis=0)

    return stiched


for t in tile_ids:
    es = possible_edges(tiles_index[t])[:4]
    count = 0
    for e in es:
        for t2 in tile_ids:
            if t == t2:
                continue
            for e2 in possible_edges(tiles_index[t2]):
                if (e == e2).all():
                    count += 1
    edge_counts[t] = count

corners = [t for t in tile_ids if edge_counts[t] == 2]
part1 = 1
for c in corners:
    part1 = part1 * c

print(f"Part 1: {part1}")

puzzle_len = 12
found_ok_corner = False

for c_prime in transpositions(tiles_index[corners[0]]):
    current = c_prime
    current_id = corners[0]
    first_in_row = c_prime
    first_in_row_id = corners[0]
    assembled = [[c_prime]]
    id_assembled = [[corners[0]]]
    row = 0
    while True:
        if len(assembled[row]) == puzzle_len:
            last = True
        else:
            last = False

        if last:
            found_match = find_match(
                first_in_row, first_in_row_id, tiles_index, tile_ids, "D"
            )
        else:
            found_match = find_match(current, current_id, tiles_index, tile_ids, "R")

        if not (found_match is None):
            if last:
                assembled.append([found_match[1]])
                first_in_row = found_match[1]
                first_in_row_id = found_match[0]
                id_assembled.append([found_match[0]])
                row += 1
            else:
                assembled[-1].append(found_match[1])
                id_assembled[-1].append(found_match[0])

            current = found_match[1]
            current_id = found_match[0]

        else:
            break

        if (len(assembled) == puzzle_len) and (len(assembled[-1]) == puzzle_len):
            stiched = stich(assembled)
            found_ok_corner = True
            break
    if found_ok_corner:
        break

sea_monster_raw = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   ",
]
sea_monster = np.array([list(x) for x in sea_monster_raw])
sea_monsters = transpositions(sea_monster)

for s in sea_monsters:
    monster_width = len(s[0])
    monster_height = len(s)
    monster_count = 0
    rough_count = sum([len([j for j in i if j == "#"]) for i in stiched])
    for x in range(len(stiched) - monster_height):
        for y in range(len(stiched[0]) - monster_width):
            matching = True
            for i in range(monster_height):
                for j in range(monster_width):
                    if s[i, j] == " ":
                        continue
                    elif s[i, j] == "#" and stiched[x + i, y + j] == ".":
                        matching = False
            if matching:
                monster_count += 1

                for i in range(monster_height):
                    for j in range(monster_width):
                        if s[i, j] == "#" and stiched[x + i, y + j] == "#":
                            rough_count -= 1
    if monster_count:
        print(rough_count)
        quit()