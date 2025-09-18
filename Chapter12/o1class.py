class Employee:
     name = "Harry"
     language = "Py"
     salary = 1200000


harry = Employee()

print(harry.name , harry.language , harry.salary) # Harry Py 1200000

rohan = Employee()
print(rohan.salary , rohan.language)

rohan.name = "Rohan"
print(rohan.name) # Rohan

# Here name is object attribute and salary and name are class attributes

# Object is a instance of a class


