import json

class Employee(dict):
    def __init__(self, name, age, address):
        dict.__init__(self, name=name, age=age, address=address)

class Address(dict):
    def __init__(self, city, street, pin):
        dict.__init__(self, city=city, street=street, pin=pin)


a=Address('ktm','boudha',2323)
e=Employee('ram',23,a)

print("Encoding object to Json")
EmployeeJsonData=json.dumps(e, indent=4)
print(EmployeeJsonData)

print("Decoding Json data")
EmployeeJson=json.loads(EmployeeJsonData)
print(EmployeeJson)