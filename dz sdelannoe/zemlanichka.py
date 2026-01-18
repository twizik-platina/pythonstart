#1. Пишем все переменные для удобства
#2. Складываем сумму собранных ягодок
#3. Вычитаем, сколько они сьели
#4.1 - Если число положительно - все айс
#4.2 - Если число отрицательно - то билебирда
#5 Выводим ответ

sobrfirst = 0 
sobrsecond = 0
sieli = 0
summasobr = 0
otvet = 0 

sobrfirst = int(input("Сколько ягод собрал первый персонаж"))
sobrsecond = int(input("Сколько ягод собрал первый персонаж"))

sieli = int(input("Сколько ягод съели"))

summa = sobrfirst + sobrsecond
otvet = summa - sieli

if sieli >= 42:
    print(f"Нифига се они обжоры")

if otvet >= 0:
    print(f"{otvet}")
else:
    print("Impossible")



