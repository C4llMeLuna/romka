a = input("введите цвет 1: ")
b = input("введите цвет 2: ")
if a == "желтый" or a == "красный" or a == "синий":
    if b == "желтый" or b == "красный" or b == "синий":
        if a == "желтый" and b == "красный" or b == "желтый" and a == "красный":
            print("оранжевый")
        elif a == "желтый" and b == "синий" or b == "желтый" and a == "синий":
            print("зеленый")
        elif a == "красный" and b == "синий" or b == "красный" and a == "синий":
            print("фиолетовый")
        else:
            print("ошибка смешивания")
    else:
        print("неправильные цвета")
else:
    print("неправильные цвета")