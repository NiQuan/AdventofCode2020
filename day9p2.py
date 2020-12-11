preamble_len = 25

with open("inputs/input9.txt", "r") as f:
    nums = [int(n) for n in f.read().splitlines()]

def sum_in_list (s, lst):
    l = len(lst)
    for i in range(l):
        for j in range(i,l):
            if lst[i] + lst[j] == s:
                return True
    return False

past_window = nums[:preamble_len]

for n in nums[preamble_len:]:
    window_lst = list(past_window)
    if sum_in_list(n, window_lst):
        past_window += [n] #Push a new number onto the queue
        past_window = past_window[1:] #Clear the oldest number from the queue
    else:
        invalid_n = n
        break

print(invalid_n)
contig_sets = []

for i in range(len(nums)):
    acc = 0
    contig_set = set()

    for j in nums[i:]:
        if acc > invalid_n:
            break
        elif acc == invalid_n:
            contig_sets += [contig_set]
        else:
            acc += j
            contig_set.add(j)

longest = []
for s in contig_sets:
    if len(s) > len(longest):
        longest = s

print(max(longest) + min(longest))

