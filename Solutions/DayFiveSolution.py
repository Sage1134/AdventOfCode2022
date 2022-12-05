import re
input = open("Inputs\DayFiveInput.txt"); lines = [i.replace("\n", "") for i in input.readlines()]

def getInitialStacks(lines):
    stackIndexes = []; stackSplit = list(lines[8]); stacks = []

    for i in range(9):
        stackIndexes.append(stackSplit.index(str(i + 1)))
    
    for y in range(9):
        stacks.append("")
        for i in range(8):
            stacks[y] += list(lines[i])[stackIndexes[y]]; stacks[y] = list(stacks[y]); stacks[y] = [i for i in stacks[y] if i != " "]
    return stacks

stacks = getInitialStacks(lines)

def getMoveInfo(line):
    moveInfo = re.findall(r"\d+", line)
    return [int(i) for i in moveInfo]

def moveCrate(stacks, amount, fromStack, toStack):
    for i in range(amount):
        crate = stacks[fromStack - 1].pop(0); stacks[toStack - 1].insert(0, crate)
    return stacks

def moveCrate9001(stacks, amount, fromStack, toStack):
    crates = list()
    for i in range(amount):
        crates.append(stacks[fromStack - 1].pop(0))
    crates.reverse()
    for x in crates:
        stacks[toStack - 1].insert(0, x)
    return stacks

for i in lines:
    if re.findall("^move", i):
        moveInfo = getMoveInfo(i); moveCrate(stacks, moveInfo[0], moveInfo[1], moveInfo[2])

topString = ""

for i in stacks:
    topString += i[0]

print(topString)

#Part Two
for i in lines:
    if re.findall("^move", i):
        moveInfo = getMoveInfo(i); moveCrate9001(stacks, moveInfo[0], moveInfo[1], moveInfo[2])

for i in stacks:
    topString += i[0]

print(topString)