"""
A SimpleKV CLI Client
"""

import requests

with requests.get('http://localhost:5000/watch', stream=True) as r:
    for line in r.iter_lines(chunk_size=10):
        print(line.decode("utf-8"))
