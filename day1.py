with open("inputs/input1.txt", "r") as f:
    lines = f.read().splitlines()

print(lines)

for i in lines:
    for j in lines:
        for k in lines:
            if int(i) + int(j) + int(k) == 2020:
                print(int(i)*int(j)*(int(k)))

        