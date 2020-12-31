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
        print(n)
        exit()

