import re
import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt

with open("inputs/input16.txt", "r") as f:
    lines = f.read().splitlines()

rule_format = re.compile("([\s\w]+):\s(\d+)-(\d+)\sor\s(\d+)-(\d+)")

rule_texts = lines[:20]
nearby_texts = lines[25:]
my_ticket = [int(x) for x in lines[22].split(",")]
rules = []

for L in rule_texts:
    matches = rule_format.match(L)
    rule = list(matches.groups())
    rule[1:] = [int(x) for x in rule[1:]]
    rules += [rule]

max_val = max([max(m[1:]) for m in rules])
prohibited = set(range(max_val + 1))

# Part 1

for r in rules:
    for n in list(range(r[1], r[2] + 1)) + list(range(r[3], r[4] + 1)):
        if n in prohibited:
            prohibited.remove(n)

error_rate = 0
valid_tickets = []

for ticket in nearby_texts:
    nums = [int(x) for x in ticket.split(",")]
    valid = True
    for n in nums:
        if n <= 0 or n > max_val or n in prohibited:
            error_rate += n
            valid = False
    if valid:
        valid_tickets += [nums]

print(error_rate)

# Part 2

possible_fields = []
for i in range(len(rules)):
    possible_fields.append(set())

final_flds = [None] * len(rules)
fld_names = [r[0] for r in rules]

# This method is assuming that there will be only a single valid position for each field
for r in rules:
    for pos in range(len(rules)):
        valid = True
        for t in valid_tickets:
            if not ((r[1] <= t[pos] <= r[2]) or (r[3] <= t[pos] <= r[4])):
                valid = False

        if valid:
            possible_fields[pos].add(r[0])

L = len(rules)
field_graph = nx.Graph()
field_graph.add_nodes_from(fld_names, bipartate=0)
field_graph.add_nodes_from(list(range(L)), bipartate=1)

for i in range(L):
    for f in possible_fields[i]:
        field_graph.add_edge(i, f)

matching = bipartite.matching.hopcroft_karp_matching(field_graph, fld_names)
print("    0123456789ABCDEFGHIJ")
for i in range(L):
    print(fld_names[i][:3], end=" ")
    for j in range(L):
        if fld_names[i] in possible_fields[j]:

            if matching[fld_names[i]] == j:
                print("X", end="")
            else:
                print("+", end="")
        else:
            print(".", end="")
    print("")

prod = 1
for f in fld_names:
    if "departure" in f:
        prod = prod * my_ticket[matching[f]]

print(prod)