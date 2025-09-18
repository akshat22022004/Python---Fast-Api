class Employee:
    language = "py"
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language} and salary is {self.salary}")

    def greet(self):
        print("Good Morning")

        
harry = Employee()
harry.language = "javascript"

harry.getInfo()
Employee.getInfo(harry)


# here language will come javascript because instance attributes will be choosen over class attributes
print(harry.language , harry.salary) 




