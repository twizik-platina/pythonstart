number = 123

first = number // 100
second = (number % 100) // 10          # Находим все циферки по отдельности
third = number % 10

min_cifra = first
if second < min_cifra:
    min_cifra = second          # Минимальная цифра
if third < min_cifra:
    min_cifra = third


max_cifra = first
if second > max_cifra:
    max_cifra = second          # Максимальная цифра (ctrl c + ctrl v спасает как никогда)
if third > max_cifra:
    max_cifra = third


print(f"Минимальная цифра числа {number} = {min_cifra}")

print(f"Максимальная цифра числа {number} = {max_cifra}")