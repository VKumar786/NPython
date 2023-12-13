'''
    TODO: Multithreading in Python | Python Tutorial - Day #97 
    ? it will try to execute process in background
    ? join say that don't execute further until function is not completed
    ? if you function is not cpu bound, but it is Input - output bound on internet
'''

import time
import threading


def func(sec):
    time.sleep(sec)
    print(f"We have waited for {sec} seconds")


# Normal Code
# start = time.time()
# func(1)
# func(2)
# func(1)
# print(time.time() - start)

# Same Code using threads
# t1 = threading.Thread(target=func, args=[1])
# t2 = threading.Thread(target=func, args=[2])
# t3 = threading.Thread(target=func, args=[1])

# start = time.time()
# t1.start()
# t2.start()
# t3.start()
# print(time.time() - start)

# Threading with join
t1 = threading.Thread(target=func, args=[1])
t2 = threading.Thread(target=func, args=[2])
t3 = threading.Thread(target=func, args=[1])

start = time.time()
t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
print(time.time() - start)
