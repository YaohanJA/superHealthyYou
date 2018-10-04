import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl.workbook import Workbook
from pandas import ExcelWriter

response = requests.get('http://www.myfoodbuddy.com/foodCalorieTable.htm')
root = BeautifulSoup(response.content,'html.parser')

table = root.select('table')[2]

bigls = []
for i in table.children:
    soup = BeautifulSoup(str(i))
    ls = []
    for i in soup.text.split('\n'):
        if i != ' ':
            ls.append(i)
    if ls:
        bigls.append(ls)

for i in bigls:
    if i == ['']:
        bigls.remove(i)

bigls[0] = bigls[0][1:7]
for i in range(len(bigls)):
    if i > 0:
        bigls[i] = bigls[i][1:6]

bigls[0][1] = bigls[0][1] + bigls[0][2].strip()
bigls[0][2] = bigls[0][3]
bigls[0][3] = bigls[0][4]
bigls[0][3] = bigls[0][5]

bigls[0].pop()
df1 = pd.DataFrame(data = bigls[1:],columns = bigls[0])

writer = pd.ExcelWriter('myFoodBuddy.xlsx')
df1.to_excel(writer,'myFoodBuddy')
writer.save()