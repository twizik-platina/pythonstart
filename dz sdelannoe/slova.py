file = open("INPUT.TXT")
data = file.read().split()
file.close()

k = int(data[0])
slovo = data[1]

izmenslovo = slovo[:k-1] + slovo[k:]

output = open("OUTPUT.TXT", "w")
output.write(izmenslovo)
output.close()