file = open("INPUT.TXT")
n = int(file.read())
file.close()

summa = 0
for i in range(1, n + 1):
    if n % i == 0:
        summa += i

output = open("OUTPUT.TXT", "w")
output.write(str(summa))
output.close()