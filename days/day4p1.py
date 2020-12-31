required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] # Not including cid

with open("inputs/input4.txt", "r") as f:
    passports = f.read().split("\n\n")

count = 0

for passport in passports:
    field_count = 0
    for field in required_fields:
        if not (field in passport):
            break
        else:
            field_count += 1
    if field_count == len(required_fields):
        count += 1

print(count)