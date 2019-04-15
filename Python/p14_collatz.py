# Project Euler Problem 14: Longest Collatz sequence

def collatz(n):
    if n % 2 == 0:
        return n/2
    else:
        return 3*n + 1

def length_sequence(n):
    length = 1
    while n != 1:
        n = collatz(n)
        length += 1
    return length


def get_sequence_length(max_n):
    largest_n = 1
    length_old = 1

    for n_start in range(1, max_n + 1):
        length_new = length_sequence(n_start)
        if length_new > length_old:
            largest_n = n_start
            length_old = length_new
    
    return largest_n

l = get_sequence_length(1000000)
print(l)
