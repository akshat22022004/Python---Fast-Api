f = open("myfile.txt","r")
lines = f.readlines() # it returns a list here 
print(lines,type(lines))
f.close()

line2 = f.readline()
print(line2 , type(line2)) 

# This  reads till there are no empty strings in there 

# with help of loop we can do in this manner
line = f.readline()
while( line != ""):
    print(line)
    line = f.readline()







