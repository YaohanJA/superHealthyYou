import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl.workbook import Workbook
from pandas import ExcelWriter
response = requests.get('https://www.nutristrategy.com/activitylist.htm')
root = BeautifulSoup(response.content,'html.parser')

table = root.select('table')[2]

bigls = []
for i in table.children:
    soup = BeautifulSoup(str(i))
    ls = []
    for i in soup.text.split('\n'):
        if i != '':
            ls.append(i)
    if ls:
        bigls.append(ls)

bigls[0][0] = bigls[0][0]+bigls[0][1].strip()
bigls[0][1] = bigls[0][2]
bigls[0][2] = bigls[0][3]
bigls[0][3] = bigls[0][4]
bigls[0][4] = bigls[0][5]

bigls[0].pop()

df2 = pd.DataFrame(data = bigls[1:],columns = bigls[0])
writer = pd.ExcelWriter('nutriStrategy.xlsx')
df2.to_excel(writer,'nutriStrategy')
writer.save()