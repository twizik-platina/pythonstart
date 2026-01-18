

n = int(input("Сколько оценок вы хотите ввести? "))
ocenki = []

print("Введите оценки:")
for i in range(n):
    ocenka = int(input(f"Оценка {i+1}: "))
    ocenki.append(ocenka)

count = 0

for ocenka in ocenki:  
    if ocenka == 5 or ocenka == 4:
        count += 1

print(f"Кол-во 4-ок и 5-ок равна = {count}")







