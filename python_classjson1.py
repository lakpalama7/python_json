import json

class devloperInfo:

    def __init__(self, name, age):
        self.name=name
        self.age=age

    def display(self):
        print("Name: ", self.name, "Age: ", self.age)


dev=devloperInfo("raju",34)

devjson={
    devloperInfo:dev,
    'salary':5000,
    'address':'india'
}

with open('developerinfo.json','w') as fp:
    json.dump(devjson, fp, indent=4, separators=(",",":"), skipkeys=True)

print("class and object write in json file")