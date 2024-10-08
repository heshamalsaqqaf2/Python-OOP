"""
 ? INHERITANCE:
   1- The concept of inheritance
   2- How to make a class inherit from another class
   3- Forms of inheritance in Python
   4- Knowing the nature of the relationship between Classes and Objects
   5- Name conflicts when inheriting more than one class
   6- Resolving name conflicts
   7- Class objects
"""

# Concept Of Inheritance
"""
 TODO: Inheritance:
  means embedding the content of a class into another class.
  In Python, a class can inherit from another class and thus get all the functions and variables in it.
  Inheritance can be used to reduce code duplication,
  for example, if you want to create a new class and you have a ready-made
  class with variables and functions that you need to write in it,
  you can make the class inherit them as they are instead of redefining them in it,
  and then you can use all the variables and functions that the new class inherited
  from the ready-made class.
"""


# How to make a class inherit from another class
# TODO: class ChildClasse(ParentClass):
# TODO: {CLassBody}


# Forms of inheritance in Python


# TODO: This is Code In Folder Inheritance


# Knowing the nature of the relationship between Classes and Objects
class A:
    pass


class B(A):
    pass


class C(B):
    pass


print("Is B inherit form A: ", issubclass(B, A))  # True
print("Is C inherit form B: ", issubclass(C, B))  # True
print("Is C inherit form A: ", issubclass(C, A))  # True
print("Is A inherit form B: ", issubclass(A, B))  # False
print("Is A inherit form C: ", issubclass(A, C))  # False

# Name conflicts when inheriting more than one class
class C(B, C):
    pass
# Resolving name conflicts

# Class objects
