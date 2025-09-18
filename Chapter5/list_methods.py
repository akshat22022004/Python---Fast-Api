friends = ["Rahul", "Rohit", "Rishabh", "Virat", "Dhawan"]
friends.append("Kohli")

print(friends) # ['Rahul', 'Rohit', 'Rishabh', 'Virat', 'Dhawan', 'Kohli']


# tell  the index and then what to insert at that index 
friends.insert(1, "Rahul") # insert at index 1
print(friends) # ['Rahul', 'Rahul', 'Rohit', 'Rishabh', 'Virat', 'Dhawan', 'Kohli']

friends.remove("Rohit")
print(friends) # ['Rahul', 'Rahul', 'Rishabh', 'Virat', 'Dhawan', 'Kohli']

friends.pop() # remove last element
print(friends) # ['Rahul', 'Rahul', 'Rishabh', 'Virat', 'Dhawan']

friends.clear() # remove all elements
print(friends) # []

friends = ["Rahul", "Rohit", "Rishabh", "Virat", "Dhawan"]
print(friends.index("Rohit")) # 1

# sorting 

l1 = [1 , 2 , 3 , 4 ,5 , 6 ]
l1.sort()
print(l1) # [1, 2, 3, 4, 5, 6]

l1.reverse()
print(l1) # [6, 5, 4, 3, 2, 1]

