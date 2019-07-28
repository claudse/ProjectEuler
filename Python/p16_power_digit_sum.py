# Project Euler Problem 16: Power Digit Sum
import time

number = 2**1000

# first solution 
start = time.clock()
str(number)

sum_digits = 0

for d in str(number):
	sum_digits += int(d)

end = time.clock()

print('Time:', end-start, 'seconds')
print('Power Digit Sum:', sum_digits)

# second solution, which is much faster
start = time.clock()

sum_digits = sum(map(int, str(number)))
end = time.clock()

print('Time:', end-start, 'seconds')
print('Power Digit Sum:', sum_digits)



