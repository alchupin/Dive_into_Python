#


import sys

digit_sum = 0
digit_string = sys.argv[1]

for ch in digit_string:
    digit_sum += int(ch)
    
print(digit_sum)
