with open("inputs/input13.txt", "r") as f:
    lines = f.read().splitlines()

earliest = int(lines[0])
busses = [int(b) for b in lines[1].split(",") if not b == "x"]
bus_delays = [(b - (earliest % b), b) for b in busses]
earliest_bus = min(bus_delays)

print(earliest_bus[1] * earliest_bus[0])