class Person:
    def __init__(self, name=None, gender=None, job=None, age=None):
        self.name = name
        self.gender = gender
        self.job = job
        self.age = age

    def print_person_info(self):
        print("Name: ", self.name)
        print("Gender: ", self.gender)
        print("Job: ", self.job)
        print("Age: ", self.age)
        print("----------------------")
