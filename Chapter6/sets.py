d = {} # empty  dictionary
print(type(d)) # <class 'dict'>

d = set() # empty set
print(type(d)) # <class 'set'>  

d = {1,2,3,4,5,6,7,8,9,10}
print(d) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(type(d)) # <class 'set'>

d = {1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10}
print(d) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

d.add(11)
print(d) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

d.remove(11)
print(d) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

d.discard(11)
print(d) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# union 
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s3 = s1.union(s2)
print(s3) # {1, 2, 3, 4, 5, 6, 7, 8}

# intersection 
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s3 = s1.intersection(s2)
print(s3) # {4, 5}

# difference 
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s3 = s1.difference(s2)
print(s3) # {1, 2, 3}

# symmetric difference 
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s3 = s1.symmetric_difference(s2)
print(s3) # {1, 2, 3, 6, 7, 8}

