class School:
    location = "Bangalore"
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def info(self):
        return f"student name {self.first_name} {self.last_name} and his age {self.age}"

    def add_location(self):
        return f"student name {self.first_name} {self.last_name} and his age {self.age} {self.location}"

    @classmethod
    def update_age(cls, new_age):
        cls.age = new_age

    @classmethod
    def split_names(cls, new_data):
        first_name = new_data[0]
        last_name = new_data[1]

        age = new_data[2]
        return cls(first_name, last_name, age)


class Tutions(School):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age)
        self.age = age
        self.location = location

    def result(self):
        return f'Student name -> {self.first_name} {self.last_name} and {self.location} {self.age}'



ini = Tutions('ram', 'gut', '28', "banaglore")
print(ini.info())