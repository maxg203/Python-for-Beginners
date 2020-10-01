class Person:
    def __int__(self,name,age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"My name is {self.name} and my age {self.age}"

    def name(self):
        return self.name
    def age(self):
        return self.age
