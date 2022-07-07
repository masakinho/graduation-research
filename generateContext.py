import json

json_open = open(綺麗だ.json, 'r')
json_load = json.load(json_open)

print(json_load)