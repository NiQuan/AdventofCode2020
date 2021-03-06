with open("inputs/input5.txt", "r") as f:
    seats = f.read().split()

def find_id(seat):
    row_pos = tuple(zip(seat[:7], range(6, -1, -1)))
    row = sum(map(lambda s: (s[0]=="B")*(2**s[1]), row_pos))

    col_pos = tuple(zip(seat[-3:], range(2, -1, -1)))
    col = sum(map(lambda s: (s[0]=="R")*(2**s[1]), col_pos))

    return row * 8 + col

IDs = list(map(find_id, seats))

myID = filter(lambda x: not (x in IDs), range(min(IDs), max(IDs) + 1))

print(list(myID))