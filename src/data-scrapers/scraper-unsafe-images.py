import os
import hashlib
import requests

# import constants
from constants_scraper_unsafe import (
    file1, filepath
)

def file_hash(file):
    with open(file, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

i = 0
hash_keys = set()

for j, line in enumerate(file1.readlines()):
    if j % 5000 == 0:
        print(f"{j} requests")
    if i >= 3500:
        break
    try:
        response = requests.get(line)
        hash = hashlib.md5(response.content).hexdigest()
        if hash not in hash_keys:
            if i % 250 == 0:
                print(f"{i} successes")
            hash_keys.add(hash)
            with open(f'{filepath}/{hash[:6]}.{line[-4:-1]}', 'wb') as f:
                f.write(response.content)
            i += 1
    except Exception:
        print("error")
        continue

