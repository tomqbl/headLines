from nltk import FreqDist
from nltk import word_tokenize
import nltk
import re
import sqlite3

connPath = '/home/fr3sh1/Documents/headlineComp/articles.db'

qByDayWyborcza = 'SELECT MIN(DATE(dtime)) as date, headline, source FROM articles WHERE headline IS NOT NULL AND source = \'wyborcza.pl\' GROUP BY headline, source;'
qByDayNiezalezna = 'SELECT MIN(DATE(dtime)) as date, headline, source FROM articles WHERE headline IS NOT NULL AND source = \'niezalezna.pl\' GROUP BY headline, source;'

qAll = 'SELECT DISTINCT headline FROM articles WHERE headline IS NOT NULL AND source IS NOT NULL'; 

#byDayNiezalezna = cur.execute(qByDayNiezalezna).fetchall()
#allSource = cur.execute(qAll).fetchall()


def fetchAllfromDB(query):
    conn = sqlite3.connect(connPath)
    cur = conn.cursor()
    return cur.execute(query).fetchall()
    conn.close()

byDayWyborcza = fetchAllfromDB(qByDayWyborcza)

def lexical_diversity(text):
    return len(set(text)) / len(text)

r = re.compile('[-+]?\\b[\\w]*\\b[-+]?')
 
def tokenizeList(varList, returnCol): #takes sql extract and outputs list of headlines
    tempList = []
    for row in varList:
        if row is not None:
            tempList.append(row[returnCol])
    tempTextString = '. '.join(tempList)
    tempTokens = []
    for w in word_tokenize(tempTextString):
        if r.search(w) is not None and len(w)>1:
            tempTokens.append(r.search(w).group())
    return tempTokens

freqDistWyb = FreqDist(tokenizeList(byDayWyborcza,1)).most_common(50)

def printEnList(listName):
    for word in enumerate(listName):
        print(word)

def cleanList(listName):
    printEnList(listName)
    exceptions = eval(input('Add exception: '))
    for exception in sorted(exceptions,reverse=True):
        print(listName[exception])
        listName.pop(exception)
    printEnList(listName)    

cleanList(freqDistWyb)
#print(nltk.pos_tag(tokenizeList(byDayWyborcza,1)))
#print(fDisTokensAll.most_common(50))

print(freqDistWyb[1][1])
