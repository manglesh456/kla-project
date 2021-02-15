import json
from PIL import Image 
from numpy import asarray 
import json
import main
for i in range(2,3):
    with open(f'Level_{i}_data\input.json') as file:
        f=json.load(file)
        print(f)
        main.wafer(f,i)
    