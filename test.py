#!/usr/bin/python3
# coding: utf-8

# In[ ]:

# a id="LinkArea:najnowsze "
# id LinkArea:Wydarzenia
# class article -> a.title


# In[27]:

from bs4 import BeautifulSoup as bs
import csv
import os.path
import datetime
import sqlite3
import requests

conn = sqlite3.connect("/home/fr3sh1/Documents/headlineComp/articles.db")
c = conn.cursor()

currentTimeStamp = datetime.datetime.now().__format__("%Y-%m-%d %X")
fileNameTimeStamp = datetime.datetime.strptime(currentTimeStamp,"%Y-%m-%d %X").strftime("%Y%m%d_%H%M%S")
gw = "wyborcza.pl"

url = "http://wyborcza.pl/0,0.html"
r = requests.get(url)
data = r.text
f = open("/home/fr3sh1/Documents/headlineComp/wyborcza/wyborcza_"+str(fileNameTimeStamp)+".html","w")
f.write(data)
f.close

soup = bs(data, 'html.parser')

#def insertRecord( newspaper,headline,link ):
#    insert = [currentTimeStamp,newspaper,headline,link]
#    c.execute("INSERT INTO test VALUES (?,?,?,?)", insert)
#    conn.commit()
#    return; 

for art in soup.find_all("article"):
    for div in art.find_all("div"):
        for tag in div.find_all('a',{"title":True}):
            print(gw,tag["title"],tag["href"])
