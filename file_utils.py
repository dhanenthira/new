import os

def file_exists(filepath):
    return os.path.exists(filepath)

def get_file_size(filepath):
    return os.path.getsize(filepath)

def read_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()
