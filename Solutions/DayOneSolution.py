input = open("File.txt")
lines = input.readlines()
Value = 0
Calories = []

for i in lines:
	if i != "\n":
		Value += int(i)
	else:
		Calories.append(Value)
		Value = 0

print(Calories.pop(Calories.index(max(Calories))) + Calories.pop(Calories.index(max(Calories))) + Calories.pop(Calories.index(max(Calories))))