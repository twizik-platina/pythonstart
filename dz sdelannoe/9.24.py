word = input("Введите слово: ")  #В нашем случае "Яблоко"


start = int(input("Начальная позиция (с 0): "))       #Ввод желаемых позиций для вырезания 
end = int(input("Конечная позиция: "))

if 0 <= start < len(word) and start <= end <= len(word):
    part = word[start:end]  #Вырез части слова
    print(f"Вырезанная часть: {part}")
else:
    print("Неправильные позиции!")