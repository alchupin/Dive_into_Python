import threading
import time

def sleeper(n, name):
    print('Привет, я {}. Собираюсь поспать.'.format(name))
    time.sleep(n)
    print('{} проснулся.'.format(name))
    
    
t = threading.Thread(target=sleeper, name='Thread1', args=[5, 'Thread1'])

thread_list = []

start = time.time()

for i in range(5):
    t = threading.Thread(target=sleeper,
                          name='thread{}'.format(i),
                          args=[5, 'thread{}'.format(i)])
    thread_list.append(t)
    t.start()
    print('{} has started'.format(t.name))
    
for t in thread_list:
    t.join()

end = time.time()
print('time taken {}'.format(end-start))


print('All threads are done.')
