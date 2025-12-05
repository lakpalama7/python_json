import json
from json import JSONEncoder

class Employee:
    def __init__(self, name, salary, address):
        self.name=name
        self.salary=salary
        self.address=address


class Address:
    def __init__(self,city,street,pin):
        self.city=city
        self.street=street
        self.pin=pin

a=Address('ktm','chabahil',4405)
e=Employee('ram',4000,a)

class EmployeeEncoder(JSONEncoder): #convert object into dict.
    def default(self, o):
        return o.__dict__
    
print("EmployeEncoding")
print(EmployeeEncoder().encode(e))

employeeJsondata=json.dumps(e, indent=4, separators=(",",":"), cls=EmployeeEncoder)
print(employeeJsondata)

print("Decode Json data")
employeedecodejson=json.loads(employeeJsondata)
print(employeedecodejson)