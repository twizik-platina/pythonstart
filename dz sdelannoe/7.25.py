


colvo5ok = 0

while True:
    ocenka = int(input("Введи оценку (0 для выхода): "))
    if ocenka == 0:
        break
    if ocenka == 5:
        colvo5ok += 1

print("Кол-во 5-ок во всем классе =",colvo5ok)