import requests
import json
from ast import literal_eval
import pandas as pd


search_url = []
search_name = ["tofu", "fish","chicken","beef","pork","shrimp","vegetarian"]

for i in range(len(search_name)):
        key = 'f9f2b94d9e7c2f5470da788737f209b'
        url = 'https://www.food2fork.com/api/search?key=' + key +'d&q='
        url = url + search_name[i]
        search_url.append(url)

contents = {}
for i in range(len(search_url)):
    contents[search_name[i]] = requests.get(search_url[i]).text


with open("/Users/qin/Desktop/food2fork_allCategory.json", "w") as f:
    json.dump(str(contents), f)


with open("/Users/qin/Desktop/food2fork_allCategory.json") as f:
    data = json.load(f) 
    data = literal_eval(data)

all_recipes = pd.DataFrame()
for key in data:
    data_dict = literal_eval(data[key])
    df = pd.DataFrame.from_dict(data_dict['recipes'])
    df["item"] = key    
    all_recipes = [all_recipes, df]
    all_recipes = pd.concat(all_recipes)

all_recipes.to_csv('/Users/qin/Desktop/food2fork_allCategories.csv', sep='\t',mode = 'w', encoding = 'utf-8')

columnsTitles=["item","title","f2f_url","image_url"]
df1 = all_recipes.drop(columns = ["source_url",'publisher', 'publisher_url', 'recipe_id','social_rank'], axis=1 )
df2=df1.reindex(columns=columnsTitles)

df2.to_csv('/Users/qin/Desktop/food2fork_fullUrl.csv', sep='\t',mode = 'w', encoding = 'utf-8')

