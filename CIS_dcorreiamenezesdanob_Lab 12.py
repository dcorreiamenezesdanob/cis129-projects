# Diego Nobrega
# Lab 12
# Convert pseudocode to python code
# Pet class

class Pet:
    # fields
    name = " "
    type = " "
    age = 0

    # constructor
    def __init__(self, name, type, age):
        self.name = name
        self.type = type
        self.age = age

    # Mutators
    def setName(self, name):
        self.name = name

    def setType(self, type):
        self.type = type

    def setAge(self, age):
        self.age = age

    # Accessors
    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getAge(self):
        return self.age


# main code
if __name__ == '__main__':

    # object of class Pet
    Animal = Pet("", "", 0)

    # input of pet name
    input_name = input("Enter a pet name:\n")
    Animal.setName(input_name)

    # input of pet type
    input_type = input("Enter a pet type:\n")
    Animal.setType(input_type)

    # input of pet age
    input_age = int(input("Enter a pet age:\n"))
    Animal.setAge(input_age)

    # animal info
    print("The pet name is ", Animal.getName())
    print("The pet type is ", Animal.getType())
    print("The pet age is ", Animal.getAge())

