import pandas as pd
import numpy as np

chars=["A.K.I.","Blanka","Cammy","Chun-Li","Dee_Jay","Dhalsim","Ed","E.Honda","Guile","Jamie","JP","Juri","Ken","Kimberly","Lily","Luke","Manon","Marisa","Rashid","Ryu","Zangief"]

all_data = pd.DataFrame()

for char in chars:
    char_tables = pd.read_html("http://api.scraperapi.com?api_key=0bac696cef224ea9bf44c064d616631f&url=https://wiki.supercombo.gg/w/Street_Fighter_6/"+char+"/Frame_data")
    char_normals = char_tables[1]
    char_normals["Type"]="Normal"
    char_specials = char_tables[11]
    char_specials["Type"]="Special"
    char_data = pd.concat([char_normals,char_specials],ignore_index=True)
    char_data["Character"]=char
    all_data = pd.concat([all_data,char_data],ignore_index=True)

all_data.drop(all_data[all_data["input"] == "input"].index,inplace=True)
all_data.drop(["Damage","Guard","Hitconfirm","Recovery","Total"],axis=1,inplace=True)
all_data.rename(columns={"input":"Input"})

all_data.to_csv("data/frames.csv",index=False)