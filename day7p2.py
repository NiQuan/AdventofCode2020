with open("inputs/input7.txt", "r") as f:
    rules = f.read().splitlines()

bag_index = {}

def count_subbags(bag, bag_index):


    total = 0
    if bag:
        total += sum(bag_index[bag][1])
        subbags = bag_index[bag]

        for i in range(len(subbags[0])):
#           print(type(subbags[0]))
            total += count_subbags(subbags[0][i], bag_index) * subbags[1][i]
    
    return total

def form_bag_names(words):
    return_list = []
    for i in range(len(words)):
        if i % 2 == 0:
            return_list += [words[i] + " " + words[i + 1]]
    return return_list
    

for r in rules:
    raw_words = r.split()
    words = [w for w in raw_words if not w in "0123456789 contain bags, bags. bag. bag,"]
    numbers = [int(w) for w in raw_words if w in "0123456789"]

    holder = words[0] + " " + words[1]
    subbags = [bag for bag in form_bag_names(words[2:]) if bag != "no other"]
    bag_index[holder] = (subbags, numbers)

count = 0

golden_subbags = count_subbags("shiny gold", bag_index)

print(golden_subbags)

