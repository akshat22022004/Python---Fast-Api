
# While loop here 
i = 1
while(i < 6):
    print(i)
    i = i + 1

l = [1,"Harry",False,"This","Rohan","Shubham","Shubh1"]
i = 0 
while(i < len(l) + 1):
     print(l[i])



# for loop 
count = 0
for i  in range(4):
       count = count + 1


l  = [1 , 4, 6, 234, 6,764]

for i  in l:
     print(i) # 1 , 4 , 6, 234,6,764

t = (6 , 231, 75 , 122)

for i in t:
     print(i) # 6 , 231 , 75 , 122

s = "Harry"

for i in s:
     print(i) # H a r r y
    
# for loop with else

for i in range(10):
     print(i)
else:
     print("Done") # 0 1 2 3 4 5 6 7 8 9 Done

# for loop with else

for i in range(10):
     if(i == 5):
          break
     print(i)

for  i in range(100):
     if(i == 5):
          continue
     print(i)   
