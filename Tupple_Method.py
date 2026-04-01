# In this Tupple is used is used in this 

# Tupple is inorder , immutable (unchanged) collection of items in python

my_tuple = (1, 2, 3)

a = (1)
print(type(a)) # this is showing integer 

# for showing the tuppel value 

b = (2,)
print(type(b))  # Tupple is shown


# some of the Tupple Methord in the js 

t = (1,2,2,3,2)
print(t.count(2))  # 3 is the out put

# Some of the Tupple Methord  are 

# index is printed in this 

t = (10,20,30,40)
print(t[0])
print(t[-1])

# slicing is used in this 

t = (1,2,3,4)
print(t[1:4])

# tupple concatination 

t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)    # (1, 2, 3, 4)

# removing the repetaion
t = (10, 20)
print(t * 3)      # (10, 20, 10, 20, 10, 20)

# tupple Comparision 

print((1, 2) == (1, 2))    # True
print((1, 2) != (2, 1))    # True
print((1, 2) < (1, 3))     # True
print((2, 1) > (1, 100))   # True

# Logical Operator 

t = (1, 2, 3)
print(t and "Hello")   # "Hello"
print(not t)           # False