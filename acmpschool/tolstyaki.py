numbers = input()
numbers_list = numbers.split()
m1 = int(numbers_list[0])
m2 = int(numbers_list[1])
m3 = int(numbers_list[2])

if 94 <= m1 <= 727 and 94 <= m2 <= 727 and 94 <= m3 <= 727:
    if m1 >= m2 and m1 >= m3:
        max = m1
    elif m2 >= m1 and m2 >= m3:
        max = m2
    else:
        max = m3
    
    print(f"{max}")  
else:
    print("Error")  
    