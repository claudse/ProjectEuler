# Project Euler Problem 17: Number letter counts

num_units = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 
	     6: 'six', 7:'seven', 8: 'eight', 9:'nine'}
num_ten_low = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',  
               15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

num_ten = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 
	   80: 'eighty', 90: 'ninety'}

# sum units
sum_units = 0
for n in num_units:
	sum_units += len(num_units[n])

# sum tens low
sum_ten_low = 0
for n in num_ten_low:
	sum_ten_low += len(num_ten_low[n])

# sum all tens
sum_tens = 0
for n in num_ten:
	sum_tens += len(num_ten[n])*10 + sum_units

sum_tens_total = sum_units + sum_ten_low + sum_tens

# sum hundreds
sum_hundreds = 0
for n in num_units:
	sum_hundreds += len(num_units[n])*100 + len('hundred')*100 + len('and')*99 + sum_tens_total

sum_total = sum_tens_total + sum_hundreds + len('one') + len('thousand')

print('The sum of all letters from 1 to 1000 is {}.'.format(sum_total)) 
