import requests 
import re
from os.path import basename
import os
import pandas as pd

frame_data = pd.read_csv("data/frames.csv")
chars = pd.unique(frame_data["Character"])

for char in chars:
    char_folder = re.sub("[\W\.\_]+","",char).lower()
    filepath = "assets/char_data/"+char_folder+"/"

    for file in os.listdir(filepath):
        filename = re.sub("-feb2024","",file)
        filename = re.sub("-aa","",filename)
        os.rename(filepath+file,filepath+filename)