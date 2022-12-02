input = open("Inputs\DayTwoInput"); lines = input.readlines()
Convert = {"A": "R", "B": "P", "C": "S"}; Score = {"R": 1, "P": 2, "S": 3}; points = 0

class RPS:
    def __init__(self, value):
        self.value = value
        if value == "R":
            self.strength = "S"; self.weakness = "P"
        elif value == "P":
            self.strength = "R"; self.weakness = "S"
        else:
            self.strength = "P"; self.weakness = "R"

    def calcMove(self, valueTwo):
        if self.value == "X":
            self.value = valueTwo.strength; self.weakness = RPS(self.value).weakness; self.strength = RPS(self.value).strength
        elif self.value == "Y":
            self.value = valueTwo.value; self.weakness = RPS(self.value).weakness; self.strength = RPS(self.value).strength
        else:
            self.value = valueTwo.weakness; self.weakness = RPS(self.value).weakness; self.strength = RPS(self.value).strength
        return self
    
    def calcPoints(self, valueTwo):
        if self.strength == valueTwo.value:
            pointsGained = 6
        elif self.weakness == valueTwo.value:
            pointsGained = 0
        else:
            pointsGained = 3
        return pointsGained + Score[self.value]

for i in lines:
    valOne = RPS(Convert[i.split(" ")[0]]); valTwo = RPS(i.split(" ")[1].replace("\n", "")).calcMove(valOne)
    points += valTwo.calcPoints(valOne)

print(points)