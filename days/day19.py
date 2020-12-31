import re

with open("inputs/input19.txt", "r") as f:
    lines = f.read()
(rule_strs, messages) = [l.splitlines() for l in lines.split("\n\n")]

rule_pattern = re.compile('(\d+)\: (\d+) ?(\d*) ?\|? ?(\d*) ?(\d*)|(\d+)\: "(\w)"')
rules = [rule_pattern.match(r).groups() for r in rule_strs]

rule_dict = {}

for r in rules:
    if r[0]:
        rule_dict[r[0]] = r
    else:
        rule_dict[r[5]] = r


def subrules(r):
    subs = []
    for sub_index in r[1:5]:
        subs.append(rule_dict.get(sub_index))
    return subs


def str_combinations(list1, list2):
    if not list1:
        return list2
    elif not list2:
        return list1
    else:
        combs = []
        for s in list1:
            for p in list2:
                combs.append(s + p)
        return combs


def all_valid_p1(r):
    if not r:
        return None
    elif r[6]:
        return [r[6]]

    valid_lst = []
    subs = subrules(r)

    valid_lst += str_combinations(all_valid_p1(subs[0]), all_valid_p1(subs[1]))
    if subs[2]:
        valid_lst += str_combinations(all_valid_p1(subs[2]), all_valid_p1(subs[3]))

    return valid_lst


def valid_p2(r):
    matches_42 = all_valid_p1(rule_dict["42"])
    matches_31 = all_valid_p1(rule_dict["31"])

    # Track if we met the requirements of the first and 2nd halves
    first_half = False
    second_half = False
    count_42 = count_31 = 0

    for i in range(0, len(r), 8):
        if r[i : i + 8] in matches_42 and not second_half:
            first_half = True
            count_42 += 1
        elif r[i : i + 8] in matches_31 and first_half:
            second_half = True
            count_31 += 1
        else:
            return False

    return second_half and (count_31 < count_42)


main_rule = rule_dict["0"]
valids = all_valid_p1(main_rule)

count_p1 = len([m for m in messages if m in valids])
count_p2 = len([m for m in messages if valid_p2(m)])

print(count_p1)
print(count_p2)