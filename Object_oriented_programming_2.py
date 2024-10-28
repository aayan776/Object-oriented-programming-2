class string_upper:
    def __init__(self):
        self.str1 = ""
    def get_string(self):
        self.str1 = input("Enter string: ")
    def string_upper(self):
        print("Uppercase of given string: ", self.str1.upper())
str1 = string_upper()
str1.get_string()
str1.string_upper()
class employee:
    def __init__(self, name):
        self.name = name
        print(f"Employee {self.name} created.")
    def __del__(self):
        print("Destructor called.")
        print(f"{self.name} deleted")
obj = employee("Tawseef")
del obj
class vehicle:
    def __init__(self, max_speed, acceleration, comfort):
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.comfort = comfort
Mercedes = vehicle(250, "30 m/s", 8)
bmw = vehicle(240, "20 m/s", 9)
print(f"The max speed of my mercedes is: {Mercedes.max_speed}.")
print(f"My mercedes accelerates at {Mercedes.acceleration}")
print(f"My mercedes comfort score is: {Mercedes.comfort}")

print(f"The max speed of my BMW is: {bmw.max_speed}.")
print(f"My BMW accelerates at {bmw.acceleration}")
print(f"My BMW comfort score is: {bmw.comfort}")
class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0
    def start_engine(self):
        print(f"The  {self.color} {self.make} {self.model} {self.year} has started its engine.")
    def accelerate(self, increment):
        self.speed += increment
        print(f"Your speed is {self.speed}")
    def brake(self, decrement):
        self.speed -= decrement
        if self.speed < 0:
            self.speed = 0
        print(f"Your speed is {self.speed}")
    def stop(self):
        self.speed = 0
        print("The car has stopped.")
    def __del__(self):
        print("Deleting car...")
car = Car("Toyota", "Corolla", 2005, "Gray")
car.start_engine()
car.accelerate(50)
car.brake(100)
car.stop()
del car
list1 = ["Tawseef", "Mamun", "Aayan", "Samayra", "Mamun", "Anaya"]
obj1 = enumerate(list1)
print(list(obj1))
expenses = [2000, 2500, 55000]
for month, expense in enumerate(expenses, start = 1):
    print(f"Month {month}: {expense}")
scores = [90, 86, 45]
names = ["Tawseef", "Mamun", "Aayan"]
for index, (name, score) in enumerate(zip(names, scores), start = 1):
    print(f"{index}. {name}: {score}")