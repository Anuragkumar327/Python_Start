

# IN THIS ALL THE METHORD OF SET ARE USED IN THE 

# creating the set 

# SETS ARE UTABLE IN NATURE AND THEY CAN BE CHANGED AFER CREATION 

# ADD THE VALUE 
# REMOVE THE ELEMENT
# UPDATE THE VALUE
# CLEAR ALL THE ELEMENTS


s1 = {1,2,3,4}

# adding the value 
s1.add(6)
s1.update([6,7])


# REMOVING THE VALUE IS 

s1.remove(3)   # error if found
s1.discard(10)  # no error if not found
x = s1.pop()   # remove the random items

# set operation in the python 

s2 = {4,5,6,8}

print(s1.union(s2))

print(s1.intersection(s2))

print(s1.difference(s2))

print(s1.symmetric_difference(s2))

# CHECKING IS USED 

print(s1.issubset(s2))

print(s1.issuperset(s2))

print(s1.isdisjoint(s2))

# copy is used in this 

s3 = s1.copy()
print(s3)