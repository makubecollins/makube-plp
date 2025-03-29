class Animal:
    """Base class for animals."""

    def __init__(self, name):
        self.name = name

    def move(self):
        """Generic move action (to be overridden)."""
        print(f"{self.name} moves.")

class Vehicle:
    """Base class for vehicles."""
    def __init__(self, model):
      self.model = model

    def move(self):
      """Generic vehicle move action (to be overridden)."""
      print(f"{self.model} moves.")

class Dog(Animal):
    """Represents a dog."""

    def move(self):
        print(f"{self.name} runs on four legs! 🐕")

class Fish(Animal):
    """Represents a fish."""

    def move(self):
        print(f"{self.name} swims. 🐟")

class Bird(Animal):
    """Represents a bird."""

    def move(self):
        print(f"{self.name} flies. 🐦")

class Car(Vehicle):
    """Represents a car."""

    def move(self):
        print(f"{self.model} is driving. 🚗")

class Plane(Vehicle):
    """Represents a plane."""

    def move(self):
        print(f"{self.model} is flying. ✈️")

class Boat(Vehicle):
    """Represents a boat."""
    def move(self):
        print(f"{self.model} is sailing. ⛵")

# Example usage:
dog = Dog("Buddy")
fish = Fish("Nemo")
bird = Bird("Tweety")
car = Car("Toyota Corolla")
plane = Plane("Boeing 747")
boat = Boat("Sailboat 3000")

animals = [dog, fish, bird]
vehicles = [car, plane, boat]

for animal in animals:
    animal.move()

print("-" * 20) #separator

for vehicle in vehicles:
    vehicle.move()