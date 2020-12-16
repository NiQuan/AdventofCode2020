with open("inputs/input12.txt", "r") as f:
    lines = f.read().splitlines()

instructions = [(line[0], int(line[1:])) for line in lines]

def next_state(inst, state):
    n = state[0]
    e = state[1]
    way_n = state[2]
    way_e = state[3]
    action = inst[0]
    value = inst[1]

    if action == "N":
        way_n += value
    elif action == "S":
        way_n -= value
    elif action == "E":
        way_e += value
    elif action == "W":
        way_e -= value

    elif action == "L":
        for i in range(value//90):
            tmp = way_e
            way_e = (-1) * way_n
            way_n = tmp
    elif action == "R":
        for i in range(value//90):
            tmp = (-1) * way_e
            way_e = way_n
            way_n = tmp
    elif action == "F":
        n += way_n * value
        e += way_e * value

    return (n, e, way_n, way_e)

state = (0, 0, 1, 10)

for instruction in instructions:
    state = next_state(instruction, state)
    print(state)

print(abs(state[0]) + abs(state[1]))
        
        

    

    

