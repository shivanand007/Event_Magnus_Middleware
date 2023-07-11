
'''
warning : - This is a sensative file don't try to edit it, without developer permissions.
'''
from dotenv import load_dotenv
import os


def write_data(data,filepath):
    os.chmod(filepath, 0o777)
    with open(filepath, 'a') as f:
        for key, value in data.items():
            f.write(f"{key},{value}\n")
    return

def read_data(filepath):
    os.chmod(filepath, 0o777)
    data = {}
    with open(filepath, 'r') as f:
        for line in f:
            key, value = line.strip().split(',')
            data[key] = value
    return data