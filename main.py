
import pandas as pd
from PIL import Image
import numpy as np
from numpy import asarray
import json
import csv
import cv2

with open('input.json') as s:
    data = json.load(s)


image1_data = Image.open('wafer_image_1.png')
image2_data = Image.open('wafer_image_2.png')
image3_data = Image.open('wafer_image_3.png')
image4_data = Image.open('wafer_image_4.png')
image5_data = Image.open('wafer_image_5.png')
data[1] = asarray(image1_data)
data[2] = asarray(image2_data)
data[3] = asarray(image3_data)
data[4] = asarray(image4_data)
data[5] = asarray(image5_data)
Result = []

image1= cv2.imread(image1)
cropped = image1[0:600, 0:800]

final = np.ndarray(shape=(6, 600, 800, 1), dtype=float, order='F')
for i in range(600):
    for j in range(800):
        for k in range(1, 6):
            final[k][i][j][0] = (data[k][i][j][0] + data[k][i][j][1] + data[k][i][j][2]) / 3
for l in range(1, 4):
    for i in range(600):
        for j in range(0, 800):
            if (final[l][i][j][0] != final[l + 1][i][j][0]) and (final[l][i][j][0] != final[l + 2][i][j][0]):
                Result.append([l, i, j])

for i in range(600):
    for j in range(0, 800):
        if (final[4][i][j][0] != final[5][i][j][0]) and (final[4][i][j][0] != final[3][i][j][0]):
            Result.append([4, i, j])

for i in range(600):
    for j in range(0, 800):
        if (final[4][i][j][0] != final[5][i][j][0]) and (final[5][i][j][0] != final[3][i][j][0]):
            Result.append([5, i, j])

df = pd.DataFrame(Result, columns=['Die', 'x', 'y'])
df.to_csv('ANS.csv')

