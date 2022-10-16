from math import atan, acos, sqrt, sin, cos, pi, atan2
from sys import argv

#
#
#

file_name = argv[1]
try:
    radius = float(argv[2])
    if radius < 1:
        raise Exception
except:
    print("Radius is wrong")
    quit()
# file_name = "input.txt"
# radius = 100
x = []
y = []
v = []

# file read
try:
    with open(file_name) as f:
        lines = list(filter(None, f.read().split('\n')))
except:
    print("File reading error")
    quit()

# file parse
i = 0
for line in lines:
    xi, yi, vi = [int(elem) for elem in line.strip().split(' ')]
    x.append(xi)
    y.append(yi)
    v.append(vi)
    i = i + 1

n = 101
m = 101
field = [[0] * n for i in range(m)]

for i in range(0, len(x)):
    field[x[i]][y[i]] += v[i]

x = []
y = []
v = []

for i in range(0, n):
    for j in range(0, m):
        if field[i][j] != 0:
            x.append(i)
            y.append(j)
            v.append(field[i][j])

v_max_global = 0
x_strike = 0
y_strike = 0

# go for every point
for i in range(0, len(x)):

    # dictionary of angles
    angles = []
    types = []
    vv = []

    v_current = 0

    # check any other point
    for j in range(0, len(x)):

        # distance between point i and j
        distance = sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)

        # distance between point O(xi - r, yi) and j
        # distance_including = sqrt((x[i] - radius - x[j]) ** 2 + (y[i] - y[j]) ** 2)

        # condition of inclusion
        if distance <= radius * 2:
            # computing the params A B
            A = atan2(y[i] - y[j], x[i] - x[j])
            B = acos(distance / 2 / radius)

            # computing the angles
            alpha = A - B
            beta = A + B

            # adding angles in the dict
            angles.append(alpha)
            types.append(1)
            vv.append(v[j])

            angles.append(beta)
            types.append(0)
            vv.append(v[j])

    # sorting the dict
    angles_type_vv = [list(x) for x in zip(angles, types, vv)]

    sorted_angels = sorted(angles_type_vv)

    # finding max v value
    v_max_local = v_current
    x_max = 0
    y_max = 0
    for element in sorted_angels:
        if element[1] == 1:
            v_current = v_current + element[2]
            if v_current > v_max_local:
                v_max_local = v_current
                x_max = x[i] - radius * cos(element[0])
                y_max = y[i] - radius * sin(element[0])
        else:
            v_current = v_current - element[2]
    if v_max_local > v_max_global:
        v_max_global = v_max_local
        x_strike = x_max
        y_strike = y_max

# print(summa)
#print("max v =", v_max_global)
print((f'%0.3f %0.3f ', x_strike, y_strike, v_max_global))





