numbers = input()
numbers_list = numbers.split()
X = int(numbers_list[0])
Y = int(numbers_list[1])
Z = int(numbers_list[2])

summa = X + Y
otvet = summa - Z

if otvet >= 0:
    print(f"{otvet}")
else:
    print(f"Impossible")
