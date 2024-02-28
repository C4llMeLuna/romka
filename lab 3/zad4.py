import random
n = 1
f = 3
while n == 1:
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    primer = a + b
    c = int(input(f"{a}" "+" f"{b}" "="))
    if c == primer:
        print("правильно")
    else:
        print("не правильно")
        f = f - 1
    if f == 0:
        print("попытки кончились")
        break