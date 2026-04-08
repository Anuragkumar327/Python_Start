student = {"Name":"Anurag jha","Age":23,"course":"Python"}

print(student.get("Age"))  # here Age is printed in this

print(student.keys()) # All the Ley value Pairs Are printed in this

print(student.values()) # all the value are printed in this like:Name,age,coure

print(student.items())  # all the items are printed

student.update({"city":"Delhi"}) # City Value is updated in this 

student.pop("Age")

student.setdefault("Hobby","Cricket")  # Addditinal data is input in this 

print(student)

"""
 dict.fromkeys(["a", "b", "c"], 0)
What it does:

It creates a NEW dictionary using a list of keys

."""


new_dict = dict.fromkeys(["a","b","c"],0)

print(new_dict)

# More some Example of this is 

subjects = ["maths","science","english"]
marks = dict.fromkeys(subjects,0)
print(marks)

# {'Math': 0, 'Science': 0, 'English': 0}