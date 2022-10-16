import random

from PIL import Image, ImageDraw
import numpy as np
from sys import argv


def generate_img(width: int, height: int):
    np.random.seed(0)
    data = np.random.rand(height, width)
    data = (data * 255).astype(np.int8)
    return Image.fromarray(data, 'L')


file_name = argv[1]

start_i = 0
start_j = int(argv[2])

img = Image.open(file_name)
#img = generate_img(1000, 1000)
# img.show()
#img.save('map.png')

map_arr_v = np.array(img)

m = len(map_arr_v[0, :])
n = len(map_arr_v[:, 0])

end_i = n - 1
end_j = int(argv[3])

map_arr_distances = np.zeros((n, m))
map_arr_distances[start_i, start_j] = map_arr_v[start_i, start_j]

map_arr_way = np.zeros((n, m))
map_arr_way[start_i, start_j] = 0

# 1 = min from right 3 = min from left 2 = min from top 4 = min from bot
# init
i = 0
for j in range(start_j + 1, m):
    map_arr_distances[i, j] = map_arr_distances[i, j - 1] + map_arr_v[i, j] + 1
    # <-- min
    map_arr_way[i, j] = 3
for j in reversed(range(0, start_j)):
    map_arr_distances[i, j] = map_arr_distances[i, j + 1] + map_arr_v[i, j] + 1
    # min -->
    map_arr_way[i, j] = 1

for i in range(1, n):
    j = 0
    map_arr_distances[i, j] = map_arr_distances[i - 1, j] + map_arr_v[i, j] + 1
    # min from top
    map_arr_way[i, j] = 2
    for j in range(1, m):
        if map_arr_distances[i, j - 1] < map_arr_distances[i - 1, j]:
            map_arr_distances[i, j] = map_arr_distances[i, j - 1] + map_arr_v[i, j] + 1
            map_arr_way[i, j] = 3
        else:
            map_arr_distances[i, j] = map_arr_distances[i - 1, j] + map_arr_v[i, j] + 1
            map_arr_way[i, j] = 2
    for j in reversed(range(0, m - 1)):
        if map_arr_distances[i, j] > (map_arr_distances[i, j + 1] + map_arr_v[i, j] + 1):
            map_arr_distances[i, j] = map_arr_distances[i, j + 1] + map_arr_v[i, j] + 1
            map_arr_way[i, j] = 1

# print(map_arr_way)

i = end_i
j = end_j

img_rgb = Image.open(file_name).convert('RGB')
# img_rgb = Image.open('map.png').convert('RGB')
draw = ImageDraw.Draw(img_rgb)
draw.point([j, i], fill="red")

while i != start_i & j != start_j:
    if map_arr_way[i, j] == 1:
        j += 1
        draw.point([j, i], fill="red")
        continue
    if map_arr_way[i, j] == 2:
        i -= 1
        draw.point([j, i], fill="red")
        continue
    if map_arr_way[i, j] == 3:
        j -= 1
        draw.point([j, i], fill="red")
        continue


img_rgb.show()
img_rgb.save('map_with_way.png')
