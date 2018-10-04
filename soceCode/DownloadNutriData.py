import pandas as pd
import urllib.request
import time

data = pd.read_csv('newLinks.csv', index_col = 0)

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

i = 0

for j in range(i, len(data)):
    url = data.iloc[i][2]
    headers={'User-Agent':user_agent,} 
    request=urllib.request.Request(url,None,headers) 
    response = urllib.request.urlopen(request)
    tab = pd.read_table(response)
    tab = tab['# Exported from https://www.nutritionvalue.org '].str.rsplit(',',expand = True, n = 2)
    tab.columns = ['Nutrient', 'Amount', 'Unit']
    tab = tab[3:]
    tab['Amount'] = tab['Amount'].astype(float)
    tab = tab[tab['Amount'] != 0]
    tab = tab[:len(tab) - 1]
    tab = tab.reset_index(drop = True) 
    file_name = str(i) + ".csv"
    print(file_name)
    tab.to_csv(file_name)
    i = i + 1
    time.sleep(5)

