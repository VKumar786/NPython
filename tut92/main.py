import time
from concurrent.futures import ThreadPoolExecutor


def func(sec):
    time.sleep(sec)
    print(f"We have waited for {sec} seconds")
    return sec


def poolingDemo():
    with ThreadPoolExecutor(max_workers=1) as executor:
        # f1 = executor.submit(func, 3)
        # f2 = executor.submit(func, 2)
        # f3 = executor.submit(func, 1)
        # f1.result()
        # f2.result()
        # f3.result()
        arr = [1, 2, 3, 1]

        results = executor.map(func, arr)

        for result in results:
            print(result)
            pass


poolingDemo()
