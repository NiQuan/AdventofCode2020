with open("inputs/input12.txt", "r") as f:
    lines = f.read().splitlines()

instructions = [(line[0], int(line[1:])) for line in lines]

def next_state(inst, state):
    n = state[0]
    e = state[1]
    direction = state[2]
    action = inst[0]
    value = inst[1]

    def move(a):
        nonlocal n
        nonlocal e
        if a == "N":
            n += value
        elif a == "S":
            n -= value
        elif a == "E":
            e += value
        elif a == "W":
            e -= value
    
    if action in "ESWN":
        move(action)
    elif action == "L":
        direction = (direction - value//90) % 4
    elif action == "R":
        direction = (direction + value//90) % 4
    elif action == "F":
        move("ESWN"[direction])

    return (n, e, direction)

state = (0, 0, 0)

for instruction in instructions:
    state = next_state(instruction, state)

print(abs(state[0]) + abs(state[1]))
        
        

    

    

