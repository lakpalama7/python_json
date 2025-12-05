import json

class Employee:
    def __init__(self, name, age, address):
        self.name=name
        self.age=age
        self.address=address

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
    
class Adress:
    def __init__(self, city, street, pin):
        self.city=city
        self.street=street
        self.pin=pin

a=Adress('ktm','boudh',3434)
e=Employee('ram',34,a)

employeeJsonData=json.dumps(e.toJson(), indent=4) #convert to json format
print(employeeJsonData)

employeeJson=json.loads(employeeJsonData)
print(employeeJson)