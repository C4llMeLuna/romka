a = int(input("введите год: "))
if a % 4 == 0 or a % 400 == 0 and a % 100 != 0:
    print(f"год {a} високосный")
else:
    print(f"год {a} не високосный")