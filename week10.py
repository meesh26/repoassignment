class Pet:

    def __init__(self, color, num_legs, breed, age):
        self.color = color
        self.num_legs = num_legs
        self.breed = breed
        self.age = age
    def go(self):

        print(f"prancing on {self.num_legs} legs and enjoying belly rubs.")

if __name__ == '__main__':
    Rex = Pet("black", 4, "lab/terrier", "9")
    Shadow = Pet("black and white", 4, "lab/beagle", "7")

    print(f"my dog, Rex, is {Rex.color} and is a {Rex.breed} mix, that is {Rex.age}.")
    print(f"my dog, Shadow, is {Shadow.color} and is a {Shadow.breed} mix, that is {Shadow.age}.")

    Shadow.go()
    Rex.go()

    animals = []
    animals.append(Shadow)
    animals.append(Rex)

    legs = 0
    for pets in animals:
        legs += pets.num_legs

    print(f"I have {legs} legs between my two pets.")