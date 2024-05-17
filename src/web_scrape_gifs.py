import requests 
import re
from bs4 import BeautifulSoup 
from os.path import basename
import os
import pandas as pd

frame_data = pd.read_csv("data/frames.csv")
chars = pd.unique(frame_data["Character"])

for char in chars:
    char_url = re.sub("\W","",char).lower()
    r = requests.get("https://ultimateframedata.com/sf6/"+char_url+"/")
    soup = BeautifulSoup(r.content) 
    for item in soup.select('img'): 
        itm = item['src']
        filename = re.sub("df\+","3",basename(itm))
        filename = re.sub("fj","j",filename)
        filename = re.sub("f\+","6",filename)
        filename = re.sub("db\+","1",filename)
        filename = re.sub("d\+","2",filename)
        filename = re.sub("b\+","4",filename)
        filename = re.sub("cr-","2",filename)
        filename = re.sub("st-","5",filename)
        filepath = "assets/char_data/"+char_url+"/"+filename
        os.makedirs(os.path.dirname(filepath),exist_ok=True)
        with open(filepath,"wb") as f:
            f.write(requests.get("https://ultimateframedata.com/sf6/"+itm).content)