class Avenger:
    def __init__(self, name, power, weapon, team):
        self.name = name
        self.power = power
        self.weapon = weapon
        self.team = team

    def display(self):
        print("Name:", self.name)
        print("Power:", self.power)
        print("Weapon:", self.weapon)
        print("Team:", self.team)
        print()


avenger1 = Avenger("Iron Man", "Technology", "Suit", "Avengers")
avenger2 = Avenger("Thor", "Thunder", "Mjolnir", "Avengers")
avenger3 = Avenger("Hulk", "Super Strength", "Fists", "Avengers")
avenger4 = Avenger("Captain America", "Super Soldier", "Shield", "Avengers")
avenger5 = Avenger("Hawkeye", "Archery", "Bow and Arrow", "Avengers")

avenger1.display()
avenger2.display()
avenger3.display()
avenger4.display()
avenger5.display()