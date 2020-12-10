with open("inputs/input7.txt", "r") as f:
    rules = f.read().splitlines()

bag_index = {}

def contains_shiny_gold(bags, bag_index):
    for bag in bags:
        new_subbags = bag_index[bag]
        if "shiny gold" in new_subbags:
            return True
        elif contains_shiny_gold(new_subbags, bag_index):
            return True
    return False

def form_bag_names(words):
    return_list = []
    for i in range(len(words)):
        if i % 2 == 0:
            return_list += [words[i] + " " + words[i + 1]]
    return return_list

for r in rules:
    raw_words = r.split()
    words = [w for w in raw_words if not w in "0123456789 contain bags, bags. bag. bag,"]
    holder = words[0] + " " + words[1]
    bag_index[holder] = [bag for bag in form_bag_names(words[2:]) if bag != "no other"]

count = 0

for bag in list(bag_index):
    if contains_shiny_gold([bag], bag_index):
        count += 1

print(count)

