import math
a = int(input("введите первое число "))
print('1.сложение')
print('2.вычитание')
print('3.умножение')
print('4.деление')
print('5.возведение в степень')
print('6.квадратный корень')
print('7.факториал')
print('8.синус')
print('9.косинус')
print('10.тангенс')
operation = input('введите номер операции ')
if operation in ["1", "2", "3", "4"]:
    b = int(input('введите второе число '))
    if operation == '1':
        print('Ответ: ',a+b)
    if operation == '2':
        print('Ответ: ',a-b)
    if operation == '3':
        print('Ответ: ',a*b)
    if operation == '4':
        if b == 0:
            print('Ошибка')
        else:
            print('Ответ: ',a/b)
elif operation in ['5','6','7','8','9','10']:
    if operation == '5':
        d = int(input("Введите степень: "))
        print('Ответ: ', a ** d)
    if operation == '6':
        if a<0:
            print('Ошибка')
        else:
            print('Ответ: ', math.sqrt(a))
    elif operation == '7':
        if a<0:
            print('Ошибка')
        else:
            print('Ответ: ', math.factorial(int(a)))
    elif operation == '8':
        print('Ответ: ', math.sin(math.radians(a)))
    elif operation == '9':
        print('Ответ: ', math.cos(math.radians(a)))
    elif operation == '10':
        print('Ответ: ', math.tan(math.radians(a)))
else:
    print('Ошибка')
r = input('Введите "r" чтобы продолжить или нажмите любую клавишу, чтобы выйти')
while r == 'r':
    g = int(input("введите первое число"))
    print('1.сложение')
    print('2.вычитание')
    print('3.умножение')
    print('4.деление')
    print('5.возведение в степень')
    print('6.квадратный корень')
    print('7.факториал')
    print('8.синус')
    print('9.косинус')
    print('10.тангенс')
    operation = input('введите номер операции')
    if operation in ["1", "2", "3", "4"]:
        b = int(input('введите второе число'))
        if operation == '1':
            print('Ответ: ', g + b)
        if operation == '2':
            print('Ответ: ', g - b)
        if operation == '3':
            print('Ответ: ', g * b)
        if operation == '4':
            if b == 0:
                print('Ошибка')
            else:
                print('Ответ: ', g / b)
    elif operation in ['5', '6', '7', '8', '9', '10']:
        if operation == '5':
            d = int(input("Введите степень: "))
            print('Ответ: ', g ** d)
        if operation == '6':
            if g < 0:
                print('Ошибка')
            else:
                print('Ответ: ', math.sqrt(g))
        elif operation == '7':
            if g < 0:
                print('Ошибка')
            else:
                print('Ответ: ', math.factorial(int(g)))
        elif operation == '8':
            print('Ответ: ', math.sin(math.radians(g)))
        elif operation == '9':
            print('Ответ: ', math.cos(math.radians(g)))
        elif operation == '10':
            print('Ответ: ', math.tan(math.radians(g)))
    else:
        print('Ошибка')
    r = input('Введите "r" чтобы продолжить или нажмите любую клавишу, чтобы выйти')
