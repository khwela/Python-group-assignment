class Pet:
    def __init__(self, name):  # Constructor to initialize the pet's attributes
        self.name = name
        self.hunger = 0
        self.energy = 10
        self.happiness = 5
        self.tricks = []  # List to store learned tricks

    def eat(self):
        self.hunger = max(0, self.hunger - 3)  # Reduce hunger by 3 but not below 0
        self.happiness = min(10, self.happiness + 1)  # Increase happiness by 1

    def sleep(self):
        self.energy = min(10, self.energy + 5)  # Increase energy by 5  not above 10

    def play(self):
        self.energy = max(0, self.energy - 2)  # Decrease energy by 2
        self.happiness = min(10, self.happiness + 2)  # Increase happiness by 2
        self.hunger = min(10, self.hunger + 1)  # Increase hunger by 1

    def get_status(self):
        print(f"Name: {self.name}")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")

    def train(self, trick):
        self.tricks.append(trick)  # Add the new trick to the list
        print(f"{self.name} has learned a new trick: {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")


print("Welcome to the Pet Simulator!")
print("")
# Create a pet
my_pet = Pet("Buddy")

# Check initial status
my_pet.get_status()
print("")

# Perform actions
my_pet.eat()
my_pet.sleep()
my_pet.play()
print("-----------------Status after actions-----------------")
# Check updated status
my_pet.get_status()

print("")

print("------------------Teach tricks-----------------")
# Teach tricks
my_pet.train("Sit")
my_pet.train("Roll over")
my_pet.show_tricks()
print("")
print("--------------------Teach more tricks-----------------")
# Teach another tricks
my_pet.train("buckle")
my_pet.train("jump")
my_pet.show_tricks()