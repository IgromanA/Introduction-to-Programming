import math

def k(n):
    return n * n

x, a= map(int, input('Enter x, a: ').split())
key = int(input('Выберите уравнение:\n' + 
                '1 - уравнение G\n' + 
                '2 - уравнение F\n' + 
                '3 - уравнение Y\n'))

if key == 1:
    if x == 0 and a == 0:
        print('Error')
    else:
        G = (2 * (56 * k(a) - 69 * a * x + 18 * k(x))) / (6 * k(a) + 25 * a * x + 24 * k(x))
        print(f'{round(G, 5)}')
elif key == 2:
    if math.cos(40 * k(a) - 27 * a * x - 7 * k(x)) == 0:
        print('Error')
    else:
        F = 1 / math.cos(40 * k(a) - 27 * a * x - 7 * k(x))
        print(f'{round(F, 5)}')
elif key == 3:
    Y = math.atan(10 * k(a) + 17 * a * x + 63 * k(x))
    print(round(Y * -1, 5))
else:
    print('Некорректное значение')