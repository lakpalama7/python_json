import json


def convertJson(obj):
    print("Create a json object")
    jobj=json.dumps(obj)
    print(jobj)

dict_obj={
    'name':'ram',
    'age':34,
    'programming':['python',  'java','html',   'css'],
    'address':'india'
}

convertJson(dict_obj)

developer={
    'name':'hari',
    'salary':3000,
    'address':'india',
    'language':['indian',   'english',   'chinese']
}

with open('developer.json','w') as fp:
    json.dump(developer, fp, indent=4, separators=("," ,":"), sort_keys=True)
print("obj write into json file done.")