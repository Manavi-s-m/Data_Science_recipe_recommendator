import pandas as pd
import random

df = pd.read_json('./data files/data.json')
print("start")
sty
count = 0
for index, row in df.iterrows():
    x = random.randint(0, 1000)
    x = int(x % 20)
    print(count)
    count+=1
    if df.loc[index, 'cuisine'] == 'others':
        df.loc[index, 'cuisine'] = cui[x]

df.to_json('C:/Users/user/IdeaProjects/Receipe predictor/data files/data2.json', orient='records')
print(df.head())
