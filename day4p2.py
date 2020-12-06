required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] # Not including cid
eye_colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

with open("inputs/input4.txt", "r") as f:
    passports = f.read().split("\n\n")

count = 0

for passport in passports:
    valid = True
    # First checking for the required fields
    field_count = 0
    for field in required_fields:
        if not (field in passport):
            break
        else:
            field_count += 1

    if field_count != len(required_fields):
        valid = False
    
    # Performing the Pt 2 validation
    split_passport = passport.split()
    for fld in split_passport:
        (name, value) = fld.split(":")

        if name == "byr":
            if not(1920 <= int(value) <= 2002):
                valid = False
        elif name == "iyr":
            if not(2010 <= int(value) <= 2020):
                valid = False
        elif name == "eyr":
            if not(2020 <= int(value) <= 2030):
                valid = False
        elif name == "hgt":
            if not value[-2:] in ["cm", "in"]:
                valid = False
            if (value[-2:] == "cm") and (not (150 <= int(value[:-2]) <= 193)):
                valid = False
            if (value[-2:] == "in") and (not (59 <= int(value[:-2]) <= 76)):
                valid = False
        elif name == "hcl":
            if not(value[0] == "#" and all(map(lambda c : c in "1234567890abcdef", value[1:]))):
                valid = False
        elif name == "ecl":
            if not value in eye_colours:
                valid = False
        elif name == "pid":
            if not(len(value) == 9 and all(map(lambda c: c in "1234567890", value))):
                valid = False

    if valid:
        count += 1



        

    

print(count)