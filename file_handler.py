import json
file="Transaction.json"

def readtransaction():
    try:
        with open(file,"r") as f:
            data=json.load(f)
            return data
    except FileNotFoundError:
        return {}
    except json.decoder.JSONDecodeError:
        return {}

def writetransaction(data):
    with open(file,"w") as f:
        json.dump(data,f)