numbers = input()
numbers_list = numbers.split()
N = int(numbers_list[0])
M = int(numbers_list[1])
K = int(numbers_list[2])

if N*M>=K:
    print("YES")
else:
    print("NO")