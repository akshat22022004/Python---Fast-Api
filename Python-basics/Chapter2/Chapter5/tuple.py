a = (1 ,2 , 3,4 ,5 ) # tuple is immutable
print(a)
b = (1,) # this is a way to make a tuple with single element 

a = (1,45,342,3424,False,"Rohan")
print(a)

no = a.count(45)
print(no) # 1

index = a.index(3424)
print(index) # 2

a = (1,2,3,4,5)
b = (6,7,8,9,10)
c = a + b
print(c) # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

