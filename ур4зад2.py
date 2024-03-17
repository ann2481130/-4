num = int(input('Введите пятизначное число:'))
print('Разряд десятков тысяч:')
digit1 = num // 10000
print(digit1)
print('Разряд тысяч:')
digit2 = (num % 10000) // 1000
print(digit2)
print('Разряд сотен:')
digit3 = (num % 1000) // 100
print(digit3)
print('Разряд десятков:')
digit4 = (num % 100)  // 10
print(digit4)
print('Разряд единиц:')
digit5 = num % 10
print(digit5)
a = digit4 ** digit5
print(a)
b = a * digit3
print(b)
c = digit1 - digit2
print(c)
d = b / c
print(d)
