input = open("Inputs\DayThreeInput"); lines = input.readlines()
priority = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"); badges = []

def findSum(chars):
    total = 0
    for i in chars:
        total += priority.index(i) + 1
    return total

def splitGroups(strings, splitVal):
    groups = []
    tempGroup = []
    for i in range(0, len(strings)):
        if (i + 1) % splitVal == 0:
            tempGroup.append(strings[i]); groups.append(tempGroup); tempGroup = []
        else:
            tempGroup.append(strings[i])
    return groups

for i in lines:
    sacs = list(map(lambda x: x.replace("\n", ""), list(i))); semiLength = int(len(sacs) / 2); sacOne = sacs[0:semiLength]; sacTwo = sacs[semiLength:(semiLength * 2)]
    for x in sacOne:
        if x in sacTwo:
            commonItem = x
            badges.append(commonItem); break

print(findSum(badges))

#Part Two
elfGroups = splitGroups(lines, 3)

for i in elfGroups:
    for x in i[0]:
        if x in i[1] and x in i[2]:
            badges.append(x); break

print(findSum(badges))