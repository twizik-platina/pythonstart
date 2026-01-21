#польз вводит символ и программа должна определить буква ли это
# если это не буква программа должна определить цифра ли это
# если это не буква и не цирфа то программа должна выдать что это неизвестный символ

symbol_kakstroka = input("введите символ:")
symbol = symbol_kakstroka[0]

print(ord(symbol))

if symbol >= "a" and symbol <= "z" or symbol >= "A" and symbol <= "Z":
    print("Это английская буква!")

    if symbol >= "a" and symbol <= "z":
        print("маленькая")
    else:
        print("большая")

elif symbol >= "0" and symbol <= "9":
    print("Это цифра")

else:
    print("Я хз, это неизвестный символ")
























