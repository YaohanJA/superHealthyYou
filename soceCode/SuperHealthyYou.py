import getUserData as gud
import webbrowser
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('chooseFoodBuddy.csv')
data = data.reset_index(drop=True)
pd.set_option('display.max_colwidth', 200)
pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows',100)

def choice(Calories):
    food_list = []
    sum = 0
    food_1 = data[data['Category'] == 'Meat And Beans'].sample(1)
    food_1_sum = food_1['Calories(kcal)'].sum()
    food_list.append(food_1['Name'].to_string(index=False))
    sum += food_1_sum
    if sum < Calories:
        food_2 = data[data['Category'] == 'Vegetable'].sample(2)
        food_2_sum = food_2['Calories(kcal)'].sum()
        food_list.append(food_2['Name'].to_string(index=False))
        sum += food_2_sum
        if sum < Calories:
            food_3 = data[data['Category'] == 'Fruit'].sample(2)
            food_3_sum = food_3['Calories(kcal)'].sum()
            food_list.append(food_3['Name'].to_string(index=False))
            sum += food_3_sum
            if sum < Calories:
                food_4 = data[data['Category'] == 'Grains'].sample(1)
                food_4_sum = food_4['Calories(kcal)'].sum()
                food_list.append(food_4['Name'].to_string(index=False))
                sum += food_4_sum
                if sum < Calories:
                    food_5 = data[data['Category'] == 'Dairy Products'].sample(1)
                    food_5_sum = food_5['Calories(kcal)'].sum()
                    food_list.append(food_5['Name'].to_string(index=False))
                    sum += food_5_sum
                    if sum < Calories:
                        food_6 = data[data['Category'] == 'Carbohydrate'].sample(1)
                        food_6_sum = food_6['Calories(kcal)'].sum()
                        food_list.append(food_6['Name'].to_string(index=False))
                        sum += food_6_sum
                        if sum < Calories:
                            food_7 = data[data['Category'] == 'Oil'].sample(1)
                            food_7_sum = food_7['Calories(kcal)'].sum()
                            food_list.append(food_7['Name'].to_string(index=False))
                            sum += food_7_sum
                            if sum < Calories:
                                food_8 = data[data['Category'] == 'Others'].sample(1)
                                food_8_sum = food_8['Calories(kcal)'].sum()
                                food_list.append(food_8['Name'].to_string(index=False))
                                sum += food_8_sum
    return food_list

calorieTup = gud.main()
foodBuddy = choice(calorieTup[1] / 2)
sportCalories = calorieTup[0]

exercise = pd.read_csv("NutriStrategyData.csv")
exercise.columns = ['level','Exercise & Calories Burned per Hour','130 lbs','155 lbs','180 lbs','205 lbs']
exercise.columns = ['level','Exercise & Calories Burned per Hour','130 lbs','155 lbs','180 lbs','205 lbs']
exercise = exercise[1:]
level_1 = exercise[exercise['level']==1.0]
level_1 = level_1.reset_index(drop = True)
level_2 = exercise[exercise['level']==2.0]
level_2 = level_2.reset_index(drop = True)
level_3 = exercise[exercise['level']==3.0]
level_3 = level_3.reset_index(drop = True)

print("Sport recommendation:\n")
if sportCalories < 252:
    print("low level: \n")
    random_l1 = np.random.choice(len(level_1), 5, replace=False)
    for i in range(0,5):
        print(level_1.iloc[random_l1[i]]['Exercise & Calories Burned per Hour'])
elif sportCalories < 370:
    print("medium level: \n")
    random_l2 = np.random.choice(len(level_2), 5, replace=False)
    for i in range(0,5):
        print(level_2.iloc[random_l2[i]]['Exercise & Calories Burned per Hour'])
else:
    print("high level: \n")
    random_l3 = np.random.choice(len(level_3), 5, replace=False)
    for i in range(0,5):
        print(level_3.iloc[random_l3[i]]['Exercise & Calories Burned per Hour'])

df_list = []

pds = pd.read_csv('newLinks.csv', index_col = 0)

for i in foodBuddy:
    if(pds['title'].str.contains(i).any()):
        pdss = pds.loc[pds['title'].str.contains(i)]
        select = pdss.sample(1)
        file = str(select.index[0]) + '.csv'
        df = pd.read_csv(file, index_col=0, header = 0)
        df['Amount'] = df['Amount'].astype(float)
        df = df[df['Amount'] > 1]
        df = df.reset_index(drop = True)
        df_list.append(df)

count = 0
print("\nHere are some ingredients for you: ")
for i in df_list:
    print("Ingredient Name: " + foodBuddy[count] + "\n")
    print(i)
    print("\n")
    count += 1

df= pd.read_csv('FoodReceipts.csv')
df=df.rename(columns = {'Receipt Name':'Recipe_Name'})


food_url = []
folder = []
for i in foodBuddy:
    if(df['Ingredients'].str.contains(i).any()):
        name = df.loc[df['Ingredients'].str.contains(i)]
        choice = name.sample(1)
        folder.append(choice['Recipe_Name'])
        food_url.append(choice['URL'])

for i in food_url:
    url = i.to_string(index=False)
    webbrowser.open(url)

def visualization(vis, df):
    recipe_name = vis.to_string(index = False)
    x = df[(df.Recipe_Name == recipe_name)].index.tolist()
    food_content = (df.iloc[x].values[0][2])
    df = pd.DataFrame()
    for i in food_content.split(','):
        temp = data[data['Name'].str.contains(i)]
        df = df.append(temp)
        df.drop_duplicates()

    new_list = pd.DataFrame(index= ['type'],columns = ['Meat And Beans','Vegetable','Fruit','Dairy Products','Grains','Oil','Others','Carbohydrate'])

    for i in new_list:
        new_list[i] = 0
    for i in list(df.iloc[:, 0]):
        new_list[i] += 1


    plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'
    plt.rcParams['axes.unicode_minus'] = False


    plt.style.use('ggplot')


    values = new_list.loc['type']

    feature = ['Meat and Beans','Vegetable','Fruit','Dairy Products','Grains','Oil','Others','Carbohydrate']

    N = len(values)

    angles=np.linspace(0, 2*np.pi, N, endpoint=False)

    values=np.concatenate((values,[values[0]]))
    angles=np.concatenate((angles,[angles[0]]))


    fig=plt.figure()
    ax = fig.add_subplot(111, polar=True)

    ax.plot(angles, values, 'o-', linewidth=2)

    ax.fill(angles, values, alpha=0.25)


    ax.set_thetagrids(angles * 180/np.pi, feature)

    ax.set_ylim(0,1.5)

    plt.title(recipe_name)


    ax.grid(True)

    plt.legend(loc = 'best')

    plt.show()

for i in folder:
    visualization(i, df)