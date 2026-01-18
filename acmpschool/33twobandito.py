

numbers = input()
numbers_list = numbers.split()
a = int(numbers_list[0])
b = int(numbers_list[1])

N = a + b - 1

aa = N - a
bb = N - b

print(f"{aa} {bb}")