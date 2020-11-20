"""
A SimpleKV CLI Client
"""

import json

import requests
import fire

default_store = "cli_store"
default_server = "http://localhost:5000"


def get_command(key):
    """
    Performs GET on KVStore
    :param key: name of the key to get
    :return: value if found in store
    """
    response = requests.get(f"{default_server}/get/{default_store}/{key}")
    resp = response.json()
    return resp['result']

def watch_command():
    """
    Performs watch on KVStore
    :return: stream of events on console
    """
    with requests.get(f'{default_server}/watch', stream=True) as r:
        for line in r.iter_lines(chunk_size=10):
            print(line.decode("utf-8"))

def put_command(key,value):
    """
    Performs PUT on KVStore
    :param key: name of the key to put
    :param value: value to put for the key
    :return: response from server
    """
    response = requests.put(f"{default_server}/put/{default_store}", 
        data=json.dumps({key:value}))
    resp = response.json()
    return resp['result']

if __name__ == "__main__":
    fire.Fire({
        "get": get_command,
        "put": put_command,
        "watch": watch_command
    })

