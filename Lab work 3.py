import math

def k(n):
    return n * n

x1, x2, a = map(int, input('Enter the limits of x, a: ').split())
key = int(input('Выберите уравнение:\n' + 
                '1 - уравнение G\n' + 
                '2 - уравнение F\n' + 
                '3 - уравнение Y\n'))

for x in range(x1, x2+1):
    if key == 1:
        if (6 * k(a) + 25 * a * x + 24 * k(x)) == 0:
            print('Error')
        else:
            G = (2 * (56 * k(a) - 69 * a * x + 18 * k(x))) / (6 * k(a) + 25 * a * x + 24 * k(x))
            print(f'x = {x}: {round(G, 5)}')
    elif key == 2:
        if math.cos(40 * k(a) - 27 * a * x - 7 * k(x)) == 0:
            print('x =', x, 'Error')
        else:
            F = 1 / math.cos(40 * k(a) - 27 * a * x - 7 * k(x))
            print(f'x = {x}: {round(F, 5)}')
    elif key == 3:
        Y = math.atan(10 * k(a) + 17 * a * x + 63 * k(x))
        print('x =', x, ':', round(Y * -1, 5))
    else:
        print('Некорректное значение')
        break