with open("inputs/input17.txt", "r") as f:
    lines = f.read().splitlines()

L = len(lines)
T = 6  # Number of steps
L_prime = L + 2 * T  # Size of grid


def empty_grid():
    return [
        [
            [["." for w in range(L_prime)] for z in range(L_prime)]
            for y in range(L_prime)
        ]
        for x in range(L_prime)
    ]


grid = empty_grid()

# Add the initial state
for i in range(L):
    for j in range(L):
        grid[L_prime // 2][L_prime // 2][i + T][j + T] = lines[i][j]


def neighbours(g, x, y, z, w):
    def offsets(a, width):
        if a == 0:
            return [0, 1]
        elif a == (width - 1):
            return [-1, 0]
        else:
            return [-1, 0, 1]

    width = len(g)
    ns = []
    for i in offsets(x, width):
        for j in offsets(y, width):
            for k in offsets(z, width):
                for l in offsets(w, width):
                    if not (i == 0 and j == 0 and k == 0 and l == 0):
                        ns.append(g[x + i][j + y][k + z][l + w])
    return ns


def step(g):
    new_g = empty_grid()

    for i in range(L_prime):
        for j in range(L_prime):
            for k in range(L_prime):
                for l in range(L_prime):
                    n = neighbours(g, i, j, k, l)
                    n_active = len([e for e in n if e == "#"])
                    if g[i][j][k][l] == "#" and (n_active in [2, 3]):
                        new_g[i][j][k][l] = "#"
                    elif g[i][j][k][l] == "." and n_active == 3:
                        new_g[i][j][k][l] = "#"
                    else:
                        new_g[i][j][k][l] = "."
    return new_g


def count_active(g):
    count = 0
    for i in range(L_prime):
        for j in range(L_prime):
            for k in range(L_prime):
                for l in range(L_prime):
                    if g[i][j][k][l] == "#":
                        count += 1
    return count


for t in range(T):
    grid = step(grid)

print(count_active(grid))