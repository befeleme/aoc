import fileinput
from itertools import product
from collections import Counter


def find_neighbors(coor):
    # calculate all neighbors from offsets
    n = [(coor[0] + x[0], coor[1] + x[1]) for x in OFFSETS]
    n.sort(key=lambda y: y[1])
    return n

def read_binary_number(pixels, image):
    bin_str = ""
    converter = {"#": "1", ".": "0"}
    for coor in pixels:
        pixel_val = image.get(coor, ".")
        bin_str += converter[pixel_val]
    return int(bin_str, 2)

def print_img(image, max_len):
    for x in range(-offset, max_len+offset):
        for y in range(-offset, max_len+offset):
            val = image.get((y,x), ".")
            print(val, end="")
        print()

def enhance(image):
    # create copy of the original image
    new_image = {}
    # process the old image:
    for pixel in image:
        bn = read_binary_number(find_neighbors(pixel), image)
        new_image[pixel] = algorithm[bn] 
    return new_image


# Each pixel has got 8 neighbors = 9 total
OFFSETS = list(product(range(-1, 2), repeat=2))

data = [line.strip() for line in fileinput.input()]
algorithm = data[0]
image = data[2:]
image_matrix = {}
max_len = len(image)
offset = 110

for y in range(-offset, max_len+offset):
    for x in range(-offset, max_len+offset):
        image_matrix[(x, y)] = "."

for col_index, row in enumerate(image):
    for row_index, char in enumerate(row):
        image_matrix[(row_index, col_index)] = char

for i in range(50):
    image_matrix = enhance(image_matrix)

c = 0
for x, y in image_matrix:
    if x <= -60:
        continue
    if y >= 160:
        continue
    else:
        if image_matrix[x, y] == "#":
            c += 1
print(c)