import concurrent.futures
import requests


def downloadFile(url, name):
    res = requests.get(url)
    open(f"tut93/{name}.jpg", "wb").write(res.content)
    return name


url = "https://picsum.photos/2000/3000"
with concurrent.futures.ProcessPoolExecutor() as executor:
    l1 = [url for i in range(5)]
    l2 = [i for i in range(5)]

    res = executor.map(downloadFile, l1, l2)
    for r in res:
        print(r)
