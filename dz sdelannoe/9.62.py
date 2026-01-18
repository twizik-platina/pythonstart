sentence = input("Введите предложение: ")          #ввод

total_chars = len(sentence)          #счет общего кол-ва букв

count_a = sentence.count('а')         #cчет буквы "а"


if total_chars > 0:
    percentage = (count_a / total_chars) * 100              #считаем процентность буковки "а"
    print(f"Букв 'а' в предложении: {count_a}")
    print(f"Всего символов: {total_chars}")                   #вывод всех данных для точности
    print(f"Доля букв 'а': {percentage}%")

else:
    print("Вы ввели пустое предложение!")                  


