import time

print("hello world")

time.sleep(2)

print("hello world")

t = time.localtime()

print(time.strftime("%Y-%m-%d", t))