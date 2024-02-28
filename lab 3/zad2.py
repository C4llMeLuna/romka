n = 1
b = " "
while n == 1:
    a = input("введите слово")
    b += (a+' ')
    if a == 'stop':
        print(b)