#coding=utf8
# Выводит лесницу их знаков #

import sys
num_steps = int(sys.argv[1])

for i in range(1, num_steps+1):
    for j in range(num_steps-i):
        print(' ', end='')
    for k in range(i):
        print('#', end='')
    print('')
