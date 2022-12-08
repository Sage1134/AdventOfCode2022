input = open("Inputs\DaySevenInput.txt")

lines = []
for i in input.readlines():
    lines.append(i.split())

for i in lines:
    if i[0] == "dir" or i[1] == "ls":
        pass
    elif i[0] !='$':
        directory[-1] += int(i[0])
    elif i [2] == '..':
        s += [directory.pop()]
        directory[-1] += s[-1]
    elif i[2] == '/':
        s, directory = [], [0]
    elif i[0] == "$" and i[1] == "cd":
        directory.append(0)

dataSize = 0
for i in s + directory[-1:]:
    if i <= 100000:
        dataSize += i

print(dataSize)

#Part Two
DataBits = []
for i in s + directory[-1:]:
    if i > sum(directory) - 40000000:
        DataBits.append(i)

print(min(DataBits))