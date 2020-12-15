with open("inputs/input11.txt", "r") as f:
    layout = [list(x) for x in f.read().splitlines()]
import copy

def neighbours(x,y,layout):
    max_x = len(layout)
    max_y = len(layout[0])
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    hits = []

    for dir in directions:
        x_prime = x
        y_prime = y

        hit = False

        while not hit:
            x_prime += dir[0]
            y_prime += dir[1]
            if not ((0 <= x_prime < max_x) and (0 <= y_prime < max_y)):
                hit = True
            elif layout[x_prime][y_prime] == "L" or layout[x_prime][y_prime] == "#":
                hit = True
                hits += layout[x_prime][y_prime]

    return hits

def new_state (ns, old_state):
    if ns.count("#") == 0 and (old_state == "L"):
        return "#"
    elif ns.count("#") >= 5 and (old_state == "#"):
        return "L"
    else:
        return old_state

def debug_print(layout): #Function for debugging
    for row in layout:
        for s in row:
            print(s, end="")
        print("")
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
