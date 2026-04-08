
# def function_Name(): In this way function is created in this

def greet():
    print("Hello ,Welcome")

greet()  # Function is called in this 

# FUNCTION WITH PARAMETER 

def greet(name):
    print("Hello",name)

greet("Kabir Jha")


# function with multiple parameter

def add(a,b):
    return (a+b)

print(add(5,6))    

# function with defalt parameter 

def welcome(name="Guest"):
    print("Welcome",name)

welcome()
welcome("kabir singh")

def get_marks():
    return [77, 86, 92]

marks = get_marks()
print("Highest:", max(marks))

# nested function is used in this 

def outer():
    print("Outer function")

    def inner():
        print("Inner function")

    inner()

outer()


# recurcive function is Used 

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))