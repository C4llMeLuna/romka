c = 1
while c == 1:
    a = str(input("Введите слово"))
    b = a.find("ф")
    if b >= 0:
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")