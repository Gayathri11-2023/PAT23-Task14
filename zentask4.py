import json
with open('data.json','r', encoding='utf-8')as file:
    data = file.read()
python_object = json.loads(data)
for item in python_object :
    print(item['name'])
