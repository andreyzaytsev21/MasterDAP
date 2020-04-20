import json

with open('data/numbers.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

k = d.items()
print(k)

k2 = sorted(k, reverse=True)
print(k2)
