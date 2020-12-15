import copy
with open("inputs/input11.txt", "r") as f:
    layout = [list(x) for x in f.read().splitlines()]

def neighbours(x,y,layout):
    n = []
    for i in range(max(0, x - 1), min(len(layout), x + 2)):
        for j in range(max(0, y - 1), min(len(layout[0]), y + 2)):
            if not (i == x and j == y):
                n += [layout[i][j]]

    return n

def new_state (ns, old_state):
    if ns.count("#") == 0 and (old_state == "L"):
        return "#"
    elif ns.count("#") >= 4 and (old_state == "#"):
        return "L"
    else:
        return old_state

def debug_print(layout): #Function for debugging
    for row in layout:
        for s in row:
            print(s, end="")
        print("")

converged = False
old_layout = copy.deepcopy(layout)
new_layout = copy.deepcopy(layout)

while not converged:
    converged = True
    for i in range(0,len(old_layout)):
        for j in range(0, len(old_layout[0])):
            ns = neighbours(i,j,old_layout)
            old = old_layout[i][j]
            new = new_state(ns, old)
            if new != old:
                converged = False
            new_layout[i][j] = new

    old_layout = copy.deepcopy(new_layout)
    
count = 0
for i in range(len(new_layout)):
    for j in range(len(new_layout[0])):
        if new_layout[i][j] == "#":
            count += 1

print(count)
