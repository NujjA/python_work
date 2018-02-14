import json

numbers = [2, 4, 6, 7, 8, 3]

filename = 'numbers.json'

with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
