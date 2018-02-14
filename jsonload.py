import json

filename = 'numbers.json'

with open(filename) as f_obj:
    print(json.load(f_obj))
    


