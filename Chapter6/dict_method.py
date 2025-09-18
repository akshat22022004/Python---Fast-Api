marks = {
    "Rohan" : 100,
    "Vishal" : 90,
    "Sameer" : 80
}
print(marks.items())  

print(marks.keys()) 

print(marks.values()) 

marks.clear()
print(marks) # {}

marks.update({"Rohan" : 100 , "Vishal" : 90 , "Sameer" : 80})
print(marks ) # {'Rohan': 100, 'Vishal': 90, 'Sameer': 80}

print(marks.get("Rohan2")) # None
print(marks["Rohan2"]) # KeyError





