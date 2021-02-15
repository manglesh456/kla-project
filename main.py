from PIL import Image 
from numpy import asarray 
import json

with open(r'Level_1_data\input.json') as file:
    f=json.load(file,)
  
# load the image and convert into  
# numpy array 
img = Image.open('Level_1_data/wafer_image_1.png') 
numpydata = asarray(img) 
  
# data 

x=0
ans=list()
for area in f['care_areas']:
    top_left=area['top_left']
    bottom_right=area['bottom_right']
    u_left=top_left['x']
    u_right=bottom_right['x']
    d_left=top_left['y']
    d_right=bottom_right['y']

    for i in range(d_right,d_left):
    
        cap=dict()
        for j in range(d_left,u_right-3):
            lt=list()
            lt.append(numpydata[i][j][0])
            lt.append(numpydata[i][j][1])
            lt.append(numpydata[i][j][2])
        
            lt2=list()
            lt2.append(numpydata[i][j+1][0])
            lt2.append(numpydata[i][j+1][1])
            lt2.append(numpydata[i][j+1][2])

            lt3=list()
            lt3.append(numpydata[i][j+2][0])
            lt3.append(numpydata[i][j+2][1])
            lt3.append(numpydata[i][j+2][2])
        
            if lt==lt3 and lt2!=lt and lt2!=lt3:
                ans.append([i,j+1])
print(ans)
