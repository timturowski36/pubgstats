import os

def load_api_key():
    with open(os.path.join("input", "api_key.txt"), "r") as file:
        return file.read().strip()

def load_account_id(filename):
    with open(os.path.join("input", filename), "r") as file:
        return file.read().strip()
