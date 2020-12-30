def parse(line):
    exp = []
    L = len(line)
    for i in range(L):
        c = line[i]
        if c in "0123456789":
            exp.append(int(c))
        elif c in "*+":
            exp.append(c)
        elif c == "(":
            subexp = ""
            depth = 1
            j = 1
            for c_prime in line[i + 1 :]:
                if depth == 0:
                    break
                subexp += c_prime
                if c_prime == ")":
                    depth -= 1
                elif c_prime == "(":
                    depth += 1
                j += 1
            end_index = i + j
            exp.append(parse(subexp))
            exp += parse(line[end_index:])
            return exp

    return exp


def eval_1(exp):
    if type(exp) == int:
        return exp
    elif type(exp) == list and len(exp) == 1:
        return exp[0]

    # Otherwise, assuming exp is a list
    op = exp[1]

    if op == "*":
        f = lambda x, y: x * y
    elif op == "+":
        f = lambda x, y: x + y

    return eval_1([f(eval_1(exp[0]), eval_1(exp[2]))] + exp[3:])


def eval_2(exp):
    if type(exp) == int:
        return exp
    op = exp[1]
    if len(exp) <= 3:
        if op == "*":
            return eval_2(exp[0]) * eval_2(exp[2])
        elif op == "+":
            return eval_2(exp[0]) + eval_2(exp[2])

    if op == "*":
        return eval_2(exp[0]) * eval_2(exp[2:])
    elif op == "+":
        return eval_2([eval_2(exp[0]) + eval_2(exp[2])] + exp[3:])


with open("inputs/input18.txt", "r") as f:
    homework = f.read().splitlines()

pt1_ans = [eval_1(parse(x)) for x in homework]
print(sum(pt1_ans))
pt2_ans = [eval_2(parse(x)) for x in homework]
print(sum(pt2_ans))
