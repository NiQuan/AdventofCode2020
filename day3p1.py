with open("input3.txt", "r") as f:
    lines = f.read().splitlines()

height = len(lines)
width = len(lines[0])

x = -3
count = 0

for y in range(0, height):
    x = (x + 3) % width
    c = lines[y][x]
    print(f"x: {x}, y:{y}, c:{c}")

    if c == "#":
        count = count + 1

print(count)

