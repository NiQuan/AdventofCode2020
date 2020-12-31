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

def terminal_acc(instructions):
    visited_insts = [False] * len(instructions)
    pointer = 0
    acc = 0

    while True:
        (new_p, new_acc) = run_instruction((pointer, acc), instructions)
        if new_p >= len(instructions):
            return acc
        elif visited_insts[new_p]:
            return None
        else:
            visited_insts[new_p] = True
            pointer = new_p
            acc = new_acc

for line in lines:
    op = line[:3]
    arg = int(line[4:])
    instructions += [(op, arg)]

for i in range(len(instructions)):
    if instructions[i][0] == "acc":
        next
    else:
        if instructions[i][0] == "nop":
            insts_prime = instructions.copy()
            insts_prime[i] = ("jmp", instructions[i][1])
        else:
            insts_prime = instructions.copy()
            insts_prime[i] = ("nop", instructions[i][1])
        final_acc = terminal_acc(insts_prime)

        if final_acc != None:
            print(final_acc)
            break