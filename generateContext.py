import json

json_open = open('綺麗だ.json', 'r', encoding="utf-8")
json_load = json.load(json_open)

result = (d.get('text') for d in json_load)
for i in result:
    print(i)
    print()
