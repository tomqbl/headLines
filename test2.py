from nltk import FreqDist
from nltk import word_tokenize
import nltk
import re
import sqlite3

conn = sqlite3.connect('/home/fr3sh1/Documents/headlineComp/articles.db')

cur = conn.cursor()

qByDayWyborcza = 'SELECT MIN(DATE(dtime)) as date, headline, source FROM articles WHERE headline IS NOT NULL AND source = \'wyborcza.pl\' GROUP BY headline, source;'
qByDayNiezalezna = 'SELECT MIN(DATE(dtime)) as date, headline, source FROM articles WHERE headline IS NOT NULL AND source = \'niezalezna.pl\' GROUP BY headline, source;'

qAll = 'SELECT DISTINCT headline FROM articles WHERE headline IS NOT NULL AND source IS NOT NULL'; 

byDayWyborcza = cur.execute(qByDayWyborcza).fetchall()
byDayNiezalezna = cur.execute(qByDayNiezalezna).fetchall()
allSource = cur.execute(qAll).fetchall()
allTextList = []
print(byDayWyborcza)
