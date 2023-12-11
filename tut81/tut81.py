'''
    TODO: Creating command line utility in python | Python Tutorial - Day #85 
'''

import argparse
import requests

# python tut81/tut81.py "https://images.pexels.com/photos/674010/pexels-photo-674010.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2" 1.jpg


def download_file(url, local_filename):
    print(type(local_filename))
    if local_filename is None or local_filename.lower() == "none":
        local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()

        with open(local_filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename


parser = argparse.ArgumentParser()
parser.add_argument("url", help="Url of file to download")
# parser.add_argument("output", help="By which name do you want to save your file")
parser.add_argument("-o", "--output",
                    help="By which name do you want to save your file", default=None)

args = parser.parse_args()

print(args.url)
print(args.output)

download_file(args.url, f"tut81/{args.output}")

# python tut81/tut81.py "https://images.pexels.com/photos/674010/pexels-photo-674010.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2" -o
