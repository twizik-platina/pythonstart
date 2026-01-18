#Ввод трехзначного числа
num = int(input("Введите трехзначное число (все цифры различны): "))


if num < 100 or num > 999:
    print("Ошибка: число должно быть трехзначным!")
else:                                                                  #Проверка, что число 3-ехзначное

    digit3 = num % 10

    digit2 = (num // 10) % 10               #Находим циферки (По названию все принципе понятно, какая цифра по счету)
    
    digit1 = num // 100
    

    if digit1 == digit2 or digit1 == digit3 or digit2 == digit3:                          #Проверка, что все цифры различны
        print("Ошибка: цифры должны быть различны!")
    else:
        print(f"Исходное число: {num}")
        print(f"Цифры: {digit1}, {digit2}, {digit3}")                  #Вывод принтами наши начальные данные и циферки для удобства просмотра
        print("Все перестановки:")
        

        print(f"1) {digit1}{digit2}{digit3}")
        print(f"2) {digit1}{digit3}{digit2}")
        print(f"3) {digit2}{digit1}{digit3}")
        print(f"4) {digit2}{digit3}{digit1}")                             #Все 6 возможных перестановок (Да благославит боженька ctrl+c и ctrl+v)
        print(f"5) {digit3}{digit1}{digit2}")
        print(f"6) {digit3}{digit2}{digit1}")