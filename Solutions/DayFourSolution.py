input = open("Inputs\DayFourInput"); lines = list(map(lambda x: x.replace("\n", ""), list(input.readlines())))
counter = 0

def structureData(line):
    return [list(map(int, line.split(",")[0].split("-"))), list(map(int, line.split(",")[1].split("-")))]

def checkContained(rangeOne, rangeTwo):
    if rangeOne[0] >= rangeTwo[0] and rangeOne[1] <= rangeTwo[1] or rangeTwo[0] >= rangeOne[0] and rangeTwo[1] <= rangeOne[1]:
        return True

for i in range(0, len(lines)):
    if checkContained(structureData(lines[i])[0], structureData(lines[i])[1]):
        counter += 1

print(counter)

#Part Two
def checkOverlap(rangeOne, rangeTwo):
    if rangeOne[0] >= rangeTwo[0] and rangeOne[0] <= rangeTwo[1] or rangeTwo[0] >= rangeOne[0] and rangeTwo[0] <= rangeOne[1]:
        return True

for i in range(0, len(lines)):
    if checkOverlap(structureData(lines[i])[0], structureData(lines[i])[1]):
        counter += 1

print(counter)