f = open("file.txt")

print(f.read())
f.close()

# With this syntax we have to not again and again close the file
# explicitly we have to not close the file
with open("file.txt") as f:
    print(f.read())

with open("file.txt") as f:
    print(f.read())

with open("file.txt") as f:
    print(f.read())