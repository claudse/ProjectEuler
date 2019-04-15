# Project Euler Problem 13: Longest Collatz sequence

with open("./data/p13_data.txt") as f:
    data = f.readlines()

largeNumbers = []
for line in data:
    largeNumbers += line.strip().split(" ")

sum_digits = 0
for i in range(len(largeNumbers)):
    sum_digits += int(largeNumbers[i])

print(sum_digits)
