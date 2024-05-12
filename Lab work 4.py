import math

def G(x, a):
    if (6 * a ** 2 + 25 * a * x + 24 * x ** 2) == 0:
        return False
    else:
        return (2 * (56 * a ** 2 - 69 * a * x + 18 * x ** 2)) / (6 * a ** 2 + 25 * a * x + 24 * x ** 2)
    
def F(x, a):
    if math.cos(40 * a ** 2 - 27 * a * x - 7 * x ** 2) == 0:
        return False
    else:
        return 1 / math.cos(40 * a ** 2 - 27 * a * x - 7 * x ** 2)

def Y(x, a):
    return  (math.atan(10 * a ** 2 + 17 * a * x + 63 * x ** 2)) * -1


x1, x2, a1, a2 = map(int, input('Enter the limits for x and a: ').split())
flag = int(input('Enter number of steps to calculate: '))
key = int(input('Choose an equation:\n' + 
                '1 - Equation G\n' + 
                '2 - Equation F\n' + 
                '3 - Equation Y\n'))
cnt = 0
ans, pairs = [], []

for a in range(a1, a2 + 1):
    for x in range(x1, x2 + 1):
        if cnt < flag:
            if key == 1:
                fun = 'G'
                if not(G(x, a)):
                    pairs.extend([0, x])
                    ans.append(pairs)
                    pairs = []
                    cnt += 1
                else:
                    pairs.extend([round(G(x, a), 5), x])
                    ans.append(pairs)
                    pairs = []
                    cnt += 1
            elif key == 2:
                fun = 'F'
                if not(F(x, a)):
                    pairs.extend([0, x])
                    ans.append(pairs)
                    pairs = []
                    cnt += 1
                else:
                    pairs.extend([round(F(x, a), 5), x])
                    ans.append(pairs)
                    pairs = []
                    cnt += 1
            elif key == 3:
                fun = 'Y'
                pairs.extend([round(Y(x, a), 5), x])
                ans.append(pairs)
                pairs = []
                cnt += 1
            else:
                break
        else:
            break

if key in [1, 2, 3]:
    print(f'x | {fun}', f'{max(ans)[1]} | {max(ans)[0]}', f'{min(ans)[1]} | {min(ans)[0]}', sep='\n')
else:
    print('Incorrect value')