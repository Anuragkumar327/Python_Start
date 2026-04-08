# CONDITION IS USED IN THE PYTHON

marks = 85

if marks >=90:
    print("Grade A")

elif marks>=75:
    print("Grade B")

elif marks >=50:
    print("Grade C")

else:
    print("Better Luck Next")


# PRINTING THE VALUE USING THE LOGICAL UNITS (AND , OR , NOT) 

age = 20
if age >=18 and age <=25:
    print("You are eligibbal for the Content")   




# Only One codition must be true 

day = "sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")


is_Raning = False

if not is_Raning:
    print("You Can Go Outside")


# NOW WE ARE PRINTING THE NESTED CONDITION IN THIS 

age = 20
has_id = True

if age>=18:
    if has_id:
        print("Entry is Allowed")

    else:
        print("id is Required in this")

else:
    print("You are underAge")            


# CONDITION IN THE DICTIONARY

student = {
    "Name": "Anurag Jha",
    "age": 22,
    "Nation": "Indian"
}    

if age in student:
    print("Age Key is existed")

else:
    print("age is Missing")    

    