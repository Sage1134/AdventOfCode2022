def iterateString(line, val):
    for i in range(val, len(line)):
        if len(set(line[i - val:i])) == len(list(line[i - val:i])):
            return i

print(iterateString(open("Inputs\DaySixInput").readlines()[0], 4), iterateString(open("Inputs\DaySixInput").readlines()[0], 14))