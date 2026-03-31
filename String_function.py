
# In this different - Different String function is used in this 

name = "anurag Kumar Jha "

print(len(name)) # print length

print(name.endswith("rag")) # True


print(name.startswith("anu"))  # True


print(name.capitalize()) # Anurag

print(name.lower()) # anurag 

print(name.strip())  # Remove the space Between both side

print(name.replace("Kumar", "parashar")) # Kumar is removed and parashar is added in this 

print(name.split(",")) # a,u,r,a,g this is spilted in this format

print(name.find("r")) 

# this Will find the letter at what index it is present 




# Bonas code for String_function all are mention in this 

text = "  Hello World  "

clean = text.strip().capitalize().replace("world","python")

print(text)

# F STRING IS USED IN THE DOWN SIDE 

name = input("Enter your Name : ")
print(f"good Afternoon  {name} ")

"""
Enter your Name : Anurag
good Afternoon  Anurag 

"""
a = 10
b = 20
print(f"the sum of the value{a+b} ")

# use of f string in the Dictionary

data = {"Name":"Anurag","Age":20}
print(f"Name:{data['Name']} , Age:{data['Age']}")

