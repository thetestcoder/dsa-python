class Person:
    name = None
    age = None
    address = None
    
    def __init__(self, name, age, address) -> None:
        self.name = name
        self.age = age
        self.address = address


name = input("Enter Yout name: ")
age = input("Enter Yout age: ")
address = input("Enter Yout address: ")


personObject = Person(name, age, address)

print("Your name is", personObject.name)
print("Your age is ", personObject.age)
print("Your Address is: ", personObject.address)