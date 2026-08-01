import json
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(BASE_DIR, "Transaction.json")

def readtransaction():
    try:
        with open(file,"r") as f:
            data=json.load(f)
            return data
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        return []

def writetransaction(data):
    print("Writing this data:", data)
    with open(file, "w") as f:
        json.dump(data, f,indent=4)