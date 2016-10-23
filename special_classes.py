class Animal:

    def __init__(self, name, species):
        print("THIS CAME FROM THE INIT METHOD")
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __del__(self):
        print("THIS CAME FROM THE DEL METHOD")


class FourLegs:
    def hasLegs(self):
        return 4


class Dog(Animal, FourLegs):
    def __init__(self, name, isBig):
        Animal.__init__(self, name, "Dog")
        self.isBig = isBig

    def getName(self):
        return self.name, self.species, self.isBig
