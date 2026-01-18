import math

number = 0

while number <= 0:
    number = float(input("Введите число для извлечения дробного корня"))

    if number<=0:
        print("Error! Вы ввели число <=0")
 

result = math.sqrt(number)

print(f"Квадратный корень из числа {number} = {result}")