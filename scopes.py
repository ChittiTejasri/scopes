#1. Local Scope
def student():
    name = "Tejasri"
    print(name)

student()
# ------------------------------------------------------
#2.Local Variable Cannot Be Used Outside
# def student():
#     Name = "sai"

# student()

# print(Name)
# ---------------------------------------------
#3.3. Global Scope
name = "Teju"

def student():
    print(name)

student()

#4.Global Variable Used Inside Function
age = 21

def show_age():
    print(age)

show_age()

#5.Local and Global Variables with Same Name
name = "Lakshmi"

def student():
    name = "Mouna"
    print(name)

student()
print(name)

#6.Using global Keyword
count = 10

def update():
    global count
    count = 20

update()

print(count)

#7.Enclosing Scope
def outer():
    name = "Shylu"

    def inner():
        print(name)

    inner()

outer()

#8.Enclosing Scope with nonlocal
def outer():
    count = 10

    def inner():
        nonlocal count
        count = 20

    inner()
    print(count)

outer()

#9.Built-in Scope
numbers = [10, 20, 30]

print(len(numbers))

#10.LEGB Rule
name = "Global"

def outer():
    name = "Enclosing"

    def inner():
        name = "Local"
        print(name)

    inner()

outer()