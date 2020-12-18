import functools

with open("inputs/input13.txt", "r") as f:
    lines = f.read().splitlines()

bus_list = lines[1].split(",")

busses = [(int(b[0]), b[1]) for b in zip(bus_list, range(len(bus_list))) if not b[0] == "x"]

def euclid(a, m):
    r_old = a
    r = m
    s = 0
    s_old = 1
    t = 1
    t_old = 0

    while r != 0:
        q = r_old // r
        (r_old, r) = (r, r_old - q * r)
        (s_old, s) = (s, s_old - q * s)
        (t_old, t) = (t, t_old - q * t)

    return (s_old)

bus_product = functools.reduce(lambda acc, x : acc * x[0], busses, 1)
part_prods = [bus_product // b[0] for b in busses]
mod_bases = [b[0] - b[1] for b in busses]
coeffs = [euclid(part_prods[i], busses[i][0]) for i in range(len(busses))]
x = [coeffs[i] * part_prods[i] * mod_bases[i] for i in range(len(busses))]

print (sum(x) % bus_product)