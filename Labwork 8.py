from random import *
from timeit import *
from math import *
from matplotlib.pyplot import *

def gen_pt(n):
    return [(uniform(0,100), uniform(0,100)) for i in range(n)]

def dist(pt1, pt2):
    return sqrt((pt2[0]-pt1[0])**2 + (pt2[1]-pt1[1])**2)

def pt_in_zone(pts, cntr, rad):
    cnt = 0
    for pt in pts:
        if dist(cntr, pt) <= rad:
            cnt += 1
    return cnt

def main():
    radius = float(input('Enter the radius: '))
    data, time = [100000 * i for i in range(1, 11)], []
    file = open('Time spent.txt', 'w')
    for data_size in data:
        pts = gen_pt(data_size)
        cntr = choice(pts)
        start_time = default_timer()
        cnt = pt_in_zone(pts, cntr, radius)
        time.append(default_timer() - start_time)
        file.write(f'Data size: {data_size} | Time spent: {default_timer() - start_time:.6f} sec | Points in circle: {cnt}\n')
    file.close()
    plot(data, time, c='c', marker='8')
    xlabel('Number of points, thous.pcs')
    ylabel('Search time, sec')
    title('Graph of dependence of search time on data size')
    grid()
    show()

if __name__ == '__main__':
    main()