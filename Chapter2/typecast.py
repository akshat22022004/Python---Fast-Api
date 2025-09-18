a = 31 
t = type(a); # class <int> 
print(t);

b = 31.0 
t = type(b); # class <float>
print(t);

c = "31"
t = type(c); # class <str>
print(t);

d = True
t = type(d); # class <bool>
print(t);


a = "31.2"
b = float(a) # a but the type should be float 
t = type(a); # class <float>

print(t);



