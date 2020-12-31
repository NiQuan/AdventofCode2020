with open("inputs/input8.txt", "r") as f:
    lines = f.read().splitlines()

instructions = []

    
def run_instruction(state, instructions):
    (pointer, acc) = state
    op = instructions[pointer][0]
    arg = instructions[pointer][1]

    if op == "acc":
        acc += arg
        pointer += 1
    elif op == "jmp":
        pointer += arg
    elif op == "nop":
        pointer += 1
    
    return (pointer, acc)

for line in lines:
    op = line[:3]
    arg = int(line[4:])
    instructions += [(op, arg)]

visited_ints = [False] * len(instructions)
loop_next = False

pointer = 0
acc = 0

while not loop_next:
    (new_p, new_acc) = run_instruction((pointer, acc), instructions)
    if visited_ints[new_p]:
        loop_next = True
    else:
        visited_ints[new_p] = True
        pointer = new_p
        acc = new_acc
        
print(acc)