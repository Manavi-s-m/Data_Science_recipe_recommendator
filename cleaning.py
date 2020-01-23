import pandas as pd
import numpy as np
import json

# data_clean() function is used to clean the available data file RAW_recipes i.e., using steps and tags columns in the original data
# file, we are getting the cuisine, dish_style and nutrition columns for the model fitting
def data_clean():
    df = pd.read_csv('./data files/RAW_recipes.csv')
    df['ingredients'] = df.ingredients.str[1:-1].str.split(',').tolist()
    # df=df[:100]
    df = df.drop(columns=['name'])

    preferences = ['bake', 'fry', 'grill', 'none']
    bake_relative = ['preheat', 'bake', 'oven', 'heat', 'stew', 'microwave']
    fry_relative = ['fry', 'sizz', 'saute', 'frizz']
    grill_relative = ['grill', 'barbecue', 'roast', 'sear']
    cuisine = ['indian', 'mexican', 'chinese', 'thai', 'italian', 'american', 'asian', 'middle-eastern', 'hawaiian', 'european','north-american']
    dish_styles = ['main-dish','desserts','frozen-desserts','appetizers','side-dishes','beverages','seasonal','soups-stews','brunch']
    for index, row in df.iterrows():
        s1 = str(row['steps'])
        s2 = str(row['tags'])
        for s in cuisine:
            if s in s2:
                df.loc[index, 'cuisine'] = s
                break
        for s in dish_styles:
            if s in s2:
                df.loc[index, 'dish_style'] = s
                break
            elif '15-minutes-or-less' in s2:
                df.loc[index, 'dish_style'] = 'side-dishes'
            else:
                df.loc[index, 'dish_style'] = 'unknown'
        for s in bake_relative:
            if s in s1:
                df.loc[index, 'style'] = "bake"
                break
        for s in fry_relative:
            if s in s1:
                df.loc[index, 'style'] = "fry"
                break
        for s in grill_relative:
            if s in s1:
                df.loc[index, 'style'] = "grill"
                break
        if pd.isna(df.loc[index, 'style']):
            df.loc[index, 'style'] = "any"

        split_nut = (df.loc[index, 'nutrition'])[1:-1].split(",")
        sum_cal = (sum(float(s) for s in split_nut))
        if sum_cal < 250:
            df.loc[index, 'nutrition'] = "low"
        elif 250 <= sum_cal < 500:
            df.loc[index, 'nutrition'] = "medium"
        elif sum_cal >= 500:
            df.loc[index, 'nutrition'] = "high"


    df.set_index('id')
    df = df.dropna()
    df = df.drop(columns=['steps'])
    df = df.drop(columns=['n_steps'])
    df = df.drop(columns=['n_ingredients'])
    df = df.drop(columns=['tags'])
    # export = df.to_json(orient='split')
    # with open('C:/Users/user/IdeaProjects/Receipe predictor/data files/data.json', 'w') as outfile:
    #     json.dump(export, outfile)
    df.to_json('C:/Users/user/IdeaProjects/Receipe predictor/data files/data.json', orient='records')
    print(df.head())
    #return df

data_clean()