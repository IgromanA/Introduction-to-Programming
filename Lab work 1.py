import math

def k(n):
    return n * n

x, a= map(int, input('Enter x, a:').split())
if (6 * k(a) + 25 * a * x + 24 * k(x)) != 0:
    G = (2 * (56 * k(a) - 69 * a * x + 18 * k(x))) / (6 * k(a) + 25 * a * x + 24 * k(x))
    print(f'{round(G, 5)}')
else:
    print('Error')

x, a= map(int, input('Enter x, a:').split())
F = 1 / math.cos(40 * k(a) - 27 * a * x - 7 * k(x))
print(f'{round(F, 5)}')

x, a= map(int, input('Enter x, a:').split())
Y = math.atan(10 * k(a) + 17 * a * x + 63 * k(x))
print(round(Y * -1, 5))