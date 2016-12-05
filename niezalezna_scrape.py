#!/usr/bin/python3
# coding: utf-8

# In[ ]:

# content of di class="tytul-glowna" (main title)
# id wydarzenia, div-> title
# div class field-field-link-wydarzenia-url-1 -> a.content


# In[15]:

from bs4 import BeautifulSoup as bs
import csv
import os.path
import datetime
import sqlite3
import requests

conn = sqlite3.connect("articles.db")
c = conn.cursor()

currentTimeStamp = datetime.datetime.now().__format__("%Y-%m-%d %X")
fileNameTimeStamp = datetime.datetime.strptime(currentTimeStamp,"%Y-%m-%d %X").strftime("%Y%m%d_%H%M%S")
niezalezna = "niezalezna.pl"

#if os.path.isfile("niezalezna.html"):
#    f = open("niezalezna.html","r")
#    data = f.read()
#    f.close
#else:
url = "http://niezalezna.pl"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
r = requests.get(url, headers=headers)
data = r.text
f = open("/home/fr3sh1/Documents/headlineComp/niezalezna/niezalezna_"+str(fileNameTimeStamp)+r".html","w")
f.write(data)
f.close

soup = bs(data, 'html.parser')

def insertRecord( newspaper,headline ):
    insert = [currentTimeStamp,newspaper,headline]
    c.execute("INSERT INTO articles VALUES (?,?,?)", insert)
    conn.commit()
    return; 

main_headline = soup.find("div",{"class":"tytul-glowna"})
insertRecord( niezalezna,main_headline.text)

sec_headlines = soup.find("div",{"id":"wydarzenia"})
for head in sec_headlines(attrs={"title":True}):
	insertRecord( niezalezna,head["title"])

for head in soup.find_all("div",{"class":"field-field-link-wydarzenia-url-1"}):
	for text in head.find_all("a"):
		insertRecord( niezalezna,text.text)
# In[ ]:


url = "http://niezalezna.pl"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
r = requests.get(url, headers=headers)
data = r.text
f = open("/home/fr3sh1/Documents/headlineComp/niezalezna/niezalezna_"+str(fileNameTimeStamp)+r".html","w")
f.write(data)
f.close

soup = bs(data, 'html.parser')


main_headline = soup.find("div",{"class":"tytul-glowna"})
insertRecord( niezalezna,main_headline.text)

sec_headlines = soup.find("div",{"id":"wydarzenia"})
for head in sec_headlines(attrs={"title":True}):
	insertRecord( niezalezna,head["title"])

for head in soup.find_all("div",{"class":"field-field-link-wydarzenia-url-1"}):
	for text in head.find_all("a"):
		insertRecord( niezalezna,text.text)


