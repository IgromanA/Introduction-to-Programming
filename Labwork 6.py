import math

class lists():
    def __init__(self, xlow, xhigh, alow, ahigh, step):
        self.xlow = xlow
        self.xhigh = xhigh
        self.alowl = alow
        self.ahigh = ahigh
        self.step = step

class func():
    def __init__(self, G, F, Y):
        self.G = G
        self.F = F
        self.Y = Y

    def funG(self, x, a):
        if (6 * a ** 2 + 25 * a * x + 24 * x ** 2) == 0:
            return 0
        else:
            return round((2 * (56 * a ** 2 - 69 * a * x + 18 * x ** 2)) / (6 * a ** 2 + 25 * a * x + 24 * x ** 2), 5)
    
    def funF(self, x, a):
        if math.cos(40 * a ** 2 - 27 * a * x - 7 * x ** 2) == 0:
            return 0
        else:
            return round(1 / math.cos(40 * a ** 2 - 27 * a * x - 7 * x ** 2), 5)

    def funY(self, x, a):
        return  round((math.atan(10 * a ** 2 + 17 * a * x + 63 * x ** 2)) * -1, 5)


x1, x2, a1, a2 = map(int, input('Enter the limits for x and a: ').split())
flag = int(input('\nEnter String of steps to calculate: '))
var = lists(x1, x2, a1, a2, flag)
cnt = 0
ans = func([], [], [])

for a in range(var.alowl, var.ahigh + 1):
    for x in range(var.xlow, var.xhigh + 1):
        if cnt < var.step:
            ans.G.append(ans.funG(x, a))
            ans.F.append(ans.funF(x, a))
            ans.Y.append(ans.funY(x, a))
            cnt += 1
        else:
            break

print(f'\nG = {ans.G}\nF = {ans.F}\nY = {ans.Y}')