class Pet:
    def __init__(self, name):
        self.name = name
        self.energy = 100
        self.hunger = 0

    def feed(self):
        self.hunger = max(self.hunger - 20, 0)
        print(f"{self.name} поїв. Голод: {self.hunger}.")

    def play(self):
        if self.energy > 10:
            self.energy -= 10
            print(f"{self.name} грається. Енергія: {self.energy}.")
        else:
            print(f"{self.name} втомлений(-а), потрібно відпочити!")

    def rest(self):
        self.energy = min(self.energy + 20, 100)
        print(f"{self.name} відпочиває. Енергія: {self.energy}.")

barcik = Pet("Барсик")

barcik.feed()
barcik.play()
barcik.rest()
