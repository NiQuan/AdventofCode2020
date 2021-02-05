mod_base = 20201227
subject = 7
pub_keys = [19774466, 7290641]


def loop_once(n, subject, mod_base):
    n = n * subject
    n = n % mod_base
    return n


def loop_k_times(subject, mod_base, k):
    n = 1
    for i in range(k):
        n = loop_once(n, subject, mod_base)
    return n


loop_sizes = []

for k in pub_keys:
    n = 1
    loop_count = 0
    while True:
        if n == k:
            loop_sizes.append(loop_count)
            break
        n = loop_once(n, subject, mod_base)
        loop_count += 1


print(loop_sizes)
print(loop_k_times(pub_keys[0], mod_base, loop_sizes[1]))
