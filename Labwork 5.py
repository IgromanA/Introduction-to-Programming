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

def main():
    x1, x2, a1, a2 = map(int, input('Enter the limits for x and a: ').split())
    flag = int(input('\nEnter String of steps to calculate: '))
    key = int(input('\nChoose an equation:\n' + 
                    '1 - Equation G\n' + 
                    '2 - Equation F\n' + 
                    '3 - Equation Y\n'))
    pat = float(input('\nEnter String pattern: '))
    cnt = 0
    ans, pairs, Nn = [], [], []
    Mark = False

    for a in range(a1, a2 + 1):
        for x in range(x1, x2 + 1):
            if cnt < flag:
                if key == 1:
                    fun = 'G'
                    if not(G(x, a)):
                        pairs.extend([0, x, a])
                        ans.append(pairs)
                        pairs = []
                        cnt += 1
                    else:
                        pairs.extend([round(G(x, a), 5), x, a])
                        ans.append(pairs)
                        pairs = []
                        cnt += 1
                elif key == 2:
                    fun = 'F'
                    if not(F(x, a)):
                        pairs.extend([0, x, a])
                        ans.append(pairs)
                        pairs = []
                        cnt += 1
                    else:
                        pairs.extend([round(F(x, a), 5), x, a])
                        ans.append(pairs)
                        pairs = []
                        cnt += 1
                elif key == 3:
                    fun = 'Y'
                    pairs.extend([round(Y(x, a), 5), x, a])
                    ans.append(pairs)
                    pairs = []
                    cnt += 1
                else:
                    break
            else:
                break

    if key in [1, 2, 3]:
        print(f'\n     x | a | {fun}\nMax: {max(ans)[1]} | {max(ans)[2]} | {float(max(ans)[0])}\nMin: {min(ans)[1]} | {min(ans)[2]} | {float(min(ans)[0])}\n')
        for i in range(len(ans)):
            print(ans[i][0], end=" ")
            if ans[i][0]== pat:
                Mark = True
                Nn.append(i+1)
        if Mark:
            print(f'\n\nString matching the pattern found\n{int(Nn[0])} sequence element\nTotal matching elements: {len(Nn)}')
        else:
            print(f'\n\nString matching the pattern not found\nTotal matching elements: 0')
    else:
        print('Incorrect value')

if __name__ == "__main__":
    main()