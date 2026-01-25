file = open("INPUT.txt")
month = int(file.read())
file.close()

if month == 12 or 1 <= month <= 2:
    text = "Winter"
elif 3 <= month <= 5:
    text = "Spring"
elif 6 <= month <= 8:
    text = "Summer"
elif 9 <= month <= 11:
    text = "Autumn"
else:
    text = "Error"

output = open("OUTPUT.txt", "w")
output.write(text)
output.close()