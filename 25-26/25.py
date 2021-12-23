f = open("input.txt", mode="r")
all_input = f.read()
f.close()
lines = all_input.split("\n")
points_mode = True
points = set()
folds = list()
for i in lines:
    if (i == ""):
        points_mode = False
        continue
    if (points_mode):
        splitted = i.split(",")
        points.add((int(splitted[0]), int(splitted[1])))
    else:
        actual = i.split(" ")[2]
        splitted = actual.split("=")
        folds.append((splitted[0], int(splitted[1])))

for i in folds:
    if i[0] == "x":
        tofold_points = set()
        for point in points:
            if (point[0] > i[1]):
                tofold_points.add(point)
        points -= tofold_points
        for point in tofold_points:
            test = i[1] - (point[0] - i[1])
            points.add((test, point[1]))
    elif i[0] == "y":
        tofold_points = set()
        for point in points:
            if (point[1] > i[1]):
                tofold_points.add(point)
        points -= tofold_points
        for point in tofold_points:
            test = i[1] - (point[1] - i[1])
            points.add((point[0], test))
    print(len(points))

# visualize
x = 1
y = 1
for i in points:
    if (i[0] > x):
        x = i[0]
    if (i[1] > y):
        y = i[1]
from PIL import Image

img = Image.new(mode="RGB", size=(x+1, y+1))

pixels = img.load()
for i in points:
    pixels[i[0], i[1]] = (255, 0, 0)
img.show()
