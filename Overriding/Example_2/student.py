from person import Person


class Student(Person):
    def __init__(self, name, age, specializations):
        
        super().__init__(name, age)
        self.specializations = specializations

    def print_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("specializations: ", self.specializations)
