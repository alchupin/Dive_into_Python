import threading
import time

def sleeper(n, name):
    print('Привет, я {}. Собираюсь поспать.'.format(name))
    time.sleep(n)
    print('{} проснулся.'.format(name))

start = time.time()

for i in range(5):
    sleeper(5, i)
    
end = time.time()

print('time taken {}'.format(end-start))
    
    
    
