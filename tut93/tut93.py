'''
    TODO: MultiProcessing in Python | Python Tutorial - Day #98 
'''

import multiprocessing
import requests


def downloadFile(url, name):
    res = requests.get(url)
    open(f"tut93/{name}.jpg", "wb").write(res.content)

    pass


url = "https://picsum.photos/2000/3000"
process = []
for _ in range(100):
    # downloadFile(url, _)
    p = multiprocessing.Process(target=downloadFile, args=[url, _])

    p.start()
    process.append(p)

for el in process:
    el.join()
