
for number in range(100, 1000):
    is_true = True
    
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_true = False
            break #Хотел принтом написать, что не подходит, но выводилось надпись (-+ понял в чем ошибка и просто брик впихнул)
            
    if is_true:
        print(number)