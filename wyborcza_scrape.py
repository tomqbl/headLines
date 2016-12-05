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

#if os.path.isfile("wyborcza.html"):
#    f = open("wyborcza.html","r")
#    data = f.read()
#    f.close
#else:
url = "http://wyborcza.pl/0,0.html"
r = requests.get(url)
data = r.text
f = open("/home/fr3sh1/Documents/headlineComp/wyborcza/wyborcza_"+str(fileNameTimeStamp)+".html","w")
f.write(data)
f.close

soup = bs(data, 'html.parser')

#fw = open("wyborcza_articles.txt","a")

def insertRecord( newspaper,headline,link ):
    insert = [currentTimeStamp,newspaper,headline,link]
    c.execute("INSERT INTO articles VALUES (?,?,?,?)", insert)
    conn.commit()
    return; 

for art in soup.find_all("article"):
    for div in art.find_all("div"):
        for tag in div.find_all('a',{"title":True}):
            insertRecord(gw,tag["title"],tag["href"])
            #print(gw,tag["title"],tag["href"])

for h in soup.find_all("h3"):            
    for art in h.find_all("a",{"id":"LinkArea:Wydarzenia", "id":"LinkArea:kraj","title":True}):
        #print(gw,art["title"],art["href"],"\n")
        insertRecord(gw,art["title"],art["href"])
    
for art in soup.find_all("a",{"id":"LinkArea:najnowsze", "title":True}):
    insertRecord(gw,art["title"],art["href"])
    #print(gw,art["title"],art["href"],"\n")
    
#Niezalezna - scrape
##Definitions
url = "http://niezalezna.pl"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
r = requests.get(url, headers=headers)
data = r.text
f = open("/home/fr3sh1/Documents/headlineComp/niezalezna/niezalezna_"+str(fileNameTimeStamp)+r".html","w")
f.write(data)
f.close

niezalezna = "niezalezna.pl"

soup = bs(data, 'html.parser')

main_headline = soup.find("div",{"class":"tytul-glowna"})
main_headline_link = main_headline.parent["href"]
insertRecord( niezalezna,main_headline.text,main_headline_link)

sec_headlines = soup.find("div",{"id":"wydarzenia"})
for head in sec_headlines(attrs={"title":True}):
	insertRecord( niezalezna,head["title"],head.parent["href"])

for head in soup.find_all("div",{"class":"field-field-link-wydarzenia-url-1"}):
    for text in head.find_all("a"):
	    insertRecord( niezalezna,text.text,text["href"])

conn.close()

#fw.close()


# In[ ]:



