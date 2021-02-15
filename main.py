
import pandas as pd
from PIL import Image
import numpy as np
from numpy import asarray
import json
import csv
import cv2

with open('input.json') as s:
    data = json.load(s)


image1 = Image.open('wafer_image_1.png')
image2 = Image.open('wafer_image_2.png')
image3 = Image.open('wafer_image_3.png')

image4 = Image.open('wafer_image_4.png')
image5 = Image.open('wafer_image_5.png')
data[1] = asarray(image1)
data[2] = asarray(image2)
data[3] = asarray(image3)
data[4] = asarray(image4)
data[5] = asarray(image5)
Result = []

image1_ROI= cv2.imread(image1)
cropped = image1[0:600, 0:800]

data_main = np.ndarray(shape=(6, 600, 800, 1), dtype=float, order='F')
for i in range(600):
    for j in range(800):
        for k in range(1, 6):
            data_main[k][i][j][0] = (data[k][i][j][0] + data[k][i][j][1] + data[k][i][j][2]) / 3
for l in range(1, 4):
    for i in range(600):
        for j in range(0, 800):
            if (data_main[l][i][j][0] != data_main[l + 1][i][j][0]) and (data_main[l][i][j][0] != data_main[l + 2][i][j][0]):
                Result.append([l, i, j])

for i in range(600):
    for j in range(0, 800):
        if (data_main[4][i][j][0] != data_main[5][i][j][0]) and (data_main[4][i][j][0] != data_main[3][i][j][0]):
            Result.append([4, i, j])

for i in range(600):
    for j in range(0, 800):
        if (data_main[4][i][j][0] != data_main[5][i][j][0]) and (data_main[5][i][j][0] != data_main[3][i][j][0]):
            Result.append([5, i, j])

df = pd.DataFrame(Result, columns=['Die', 'x', 'y'])
df.to_csv('outputc.csv')
