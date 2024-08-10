"""
 ? CLASS AND OBJECT:
   1- The concept of classics
   2- Object concept
   3- Class definition
   4- The concept of properties
   5- The word self
   6- Function __init__()
   7- Relationship between class and object
"""


# Class Concept:
# TODO: Class This is a container that can contain functions, variables, arrays, etc.
# Class Definition
class Person1:
    name = None  # Properties
    agee = None  # Properties
    Study = None  # Properties


gazeObject = Person1()
heshamObject = Person1()
# ------------------------------------------------


# Object Concept:
# TODO: Object is a copy of the class.
class Person:
    name = None
    str()


p = Person()  # This is Object
p.name = "Gaze"
print(p.name)
# ------------------------------------------------

# Concept Of Properties
p1 = Person()
p2 = Person()
p1.name = "Gaze"
p2.name = "Hesham"
print(p1.name)
print(p2.name)
# ------------------------------------------------


# The Word Self
class Compartor:
    def print_max(self, a, b):
        if a > b:
            print(a, "A Is Bigger")
        elif a < b:
            print(b, " B Is Bigger")
        else:
            print("The Equal Tow Numbers")


compartor = Compartor()
compartor.print_max(2, 6)
# ------------------------------------------------


# Function __init__()
class Person3:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("------------------")


# p1 = Person3("Gaze", 23)
hesham = Person3("Hesham", 24)
gaze = Person3("Gaze", 23)
gaze.print_info()
hesham.print_info()
# ------------------------------------------------

# Relationship Between Class And Object
"""
  TODO: Class:
  The basic idea of a class is to set up a common format for storing data and provide user-friendly
    ways to access and manipulate that data seamlessly. 
    By its very nature, 
    Glass doesn't store any information,
    which is why it's called a Blue Print.

  TODO: Object:
  The basic idea of an object is to create a replica of the Glass and insert the data
    you want into it while respecting any conditions set in the original Glass. 
    So you can't create an object without a class because
    an object by its very nature is a copy of a specific class.
"""
