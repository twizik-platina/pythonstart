numbers = input()
numbers_list = numbers.split()
a = int(numbers_list[0])
b = int(numbers_list[1])
c = int(numbers_list[2])


if a >= b and a >= c:
    max_salary = a
elif b >= a and b >= c:
    max_salary = b
else:
    max_salary = c

if a <= b and a <= c:
    min_salary = a
elif b <= a and b <= c:
    min_salary = b
else:
    min_salary = c

    
raz = max_salary - min_salary
print(raz)