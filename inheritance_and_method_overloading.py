class TataBusiness:
    def __init__(self, others):
        self.founder = "JRD Tata"
        self.automobile = "Automobile"
        self.hospitality = "Hotels"
        self.consulting = "Consulting"
        self.other_business = others

    def info(self):
        return f"Founder {self.founder} and the Operating business {self.automobile}, {self.hospitality}, " \
               f"{self.consulting} and cars which they produce {self.other_business}"


class AutomobileIndustry(TataBusiness):
    def __init__(self, *cars):  # Passing multiple arguments
        self.cars = cars
        super().__init__(self.cars)

    def cars_models(self):
        return {"Cars": self.cars[0]}

    def info(self):   # Method overloading from Parent(info) to Child(info)
        return f"Cars from tata: {self.cars[0]}"

    def calling_info_from_parent_class(self):
        return super().info()


class Hotels(TataBusiness):
    def __init__(self, *args):
        self.hotels = args
        super().__init__(self.hotels)

    def hotels_info(self):
        return {"Hotels": ["Taj Hotels", "Indian Hotels"]}


class MultipleInheritance(AutomobileIndustry, Hotels):
    def __init__(self, *args):
        self.cars = args
        super().__init__(self.cars)

    def call_all_fun(self):
        return super().calling_info_from_parent_class(), super().hotels_info()


obj = AutomobileIndustry(["Tigor", "Nexon", "Harrier"])
print(obj.cars_models())
print(obj.info())
print(obj.calling_info_from_parent_class())


obj1 = MultipleInheritance({"cars": ["Tigor", "Nexon", "Harrier"], "hotels": ["Taj Hotels", "Indian Hotels"]})
print(obj1.call_all_fun())

# Verifying MRO(Method Resolution Order)
print(MultipleInheritance.__mro__)
