"""
  ? CONSTANT FUNCTIONS:
  1- Concept Static Functions
  2- Example of Static Methods.
"""


class StaticFunctions:

    # TODO: Can You Access Function Form Class Name Directed.
    @staticmethod
    def function_static():
        print("This Is Static Functions")

    def function_normal(self):
        print("This Is Normal Functions")


# ? Access Methods Static
StaticFunctions.function_static()
