#coding=utf8

import threading
import time

def sleeper(n, name):
    print('Привет, я {}. Собираюсь поспать.'.format(name))
    time.sleep(n)
    print('{} проснулся'.format(name))
    
t = threading.Thread(target=sleeper, name='Thread1', args=(3, 'Thread1'))

t.start()
t.join()
print('Hello')

