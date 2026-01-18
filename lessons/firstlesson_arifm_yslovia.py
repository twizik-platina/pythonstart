
 # общие числа(сам билет, левая и правая части и числа с каждой части отдельно)

ticket = 0
left_part = 0
right_part = 0

digit_num1 = 0
digit_num2 = 0
digit_num3 = 0

sum_left = 0
sum_right = 0



ticket = int( input("Номерок билета напиши") )

left_part = ticket // 1000
right_part = ticket % 1000


digit_num1 = left_part // 100
digit_num2 = (left_part % 100) // 10
digit_num3 = left_part % 10

sum_left = digit_num1 + digit_num2 + digit_num3 # находим сумму левой части билета

digit_num1 = right_part // 100
digit_num2 = (right_part % 100) // 10
digit_num3 = right_part % 10

sum_right = digit_num1 + digit_num2 + digit_num3 # находим сумму правой части билета

# print(f"sum_left = {sum_left} sum_right = {sum_right}")


1
if sum_left == sum_right:
    print("Поздравляем, ваш билетик счастливый")
else:
    print("Не в этот раз...")






