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


def all_valid(r):
    if not r:
        return None
    elif r[6]:
        return [r[6]]

    valid_lst = []
    subs = subrules(r)

    valid_lst += str_combinations(all_valid(subs[0]), all_valid(subs[1]))
    if subs[2]:
        valid_lst += str_combinations(all_valid(subs[2]), all_valid(subs[3]))

    return valid_lst


main_rule = rule_dict["0"]
valids = all_valid(main_rule)

count = len([m for m in messages if m in valids])

print(count)