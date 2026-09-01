t = () # empty tuple
print(type(t))

# for empty sets 
s = set()  # empty sets
print(type(s))

a = {"738", "ujjwal", "82378" , "746" , "738"}
print(a)

print(len(a))
a.remove("738")
print(a)

# union and intersection 

b = {"1","2","3","4"} # {'5', '1', '6', '4', '2', '3'}
c = {"3","4","5","6"} # {'3', '4'}

print(b.union(c))
print(b.intersection(c))