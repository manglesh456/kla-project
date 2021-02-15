from PIL import Image 
from numpy import asarray 
import json
import csv
def wafer(fa,i):
    row=fa['die']['rows']
    col=fa['die']['columns']
    
    
    for x in range(row*col):#image number
        img = Image.open(f'Level_{i}_data/wafer_image_{x+1}.png') 
        caller(fa,x+1,img)

def caller(f,img_num,img):
    numpydata = asarray(img).tolist() 

    for i in f['exclusion_zones']:
        top_left=i['top_left']
        bottom_right=i['bottom_right']
        u_left=top_left['x']
        u_right=bottom_right['x']
        d_left=top_left['y']
        d_right=bottom_right['y']

        for i in range(d_right,d_left):
    
            cap=dict()
            for j in range(d_left,u_right-3):
                numpydata[i][j][0]=-22222
                numpydata[i][j][1]=-22222
                numpydata[i][j][2]=-22222
# data 

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
                if numpydata[i][j][0]==-22222 and numpydata[i][j][1]==-22222 and numpydata[i][j][2]==-22222:
                    continue
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
                    with open('data.csv','a') as file:
                        csvwriter=csv.writer(file)
                        csvwriter.writerow((img_num,j,i))
