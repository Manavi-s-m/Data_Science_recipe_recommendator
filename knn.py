from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from scipy.sparse import csr_matrix

import json
import codecs
import pandas as pd
import numpy as np
import time

start_time = time.time()
meal_id, cuisine, ingredients, ingre, main_dataset, train_set, test_set = [], [], [], [], [], [], []
predicted_cuisine = ''


# creates all the lists needed for the execution
def lists(filename):
    with codecs.open(filename, encoding='utf-8') as data_file:
        data = json.load(data_file)

    # print(type(data))
    for i in range(0, len(data)):
        meal_id.append(data[i]["id"])
        cuisine.append(data[i]["cuisine"])
        ingredients.append(data[i]["ingredients"])

    for i in ingredients:
        temp = u''
        for j in range(len(i)):
            temp = temp + u" " + i[j]
        ingre.append(temp.encode('utf-8'))
    return meal_id


# vectorizes the columns in the data and convert them into features
def ing_vector(existing, user_ing):
    existing.append(user_ing)
    vector = TfidfVectorizer(use_idf=True, stop_words='english', max_features=1000)
    ing_vect = vector.fit_transform(existing)
    return ing_vect.todense()


# training the knn model for the future prediction
def KNN_trainer(train_set, cuisine, n):
    close = KNeighborsClassifier(n_neighbors=int(n))
    return close.fit(train_set, cuisine)


# user is asked to enter pantry availability and user preferences i.e., cooking style, cooking time, calories level
def KNN_predictor(test_set, close, neighbors):
    neighbors = int(neighbors)
    print("")
    predicted_cuisine = close.predict_proba(test_set)[0]
    predicted_single_cuisine = close.predict(test_set)
    predicted_class = close.classes_
    print("The model predicts that the ingredients resembles %s" % (predicted_single_cuisine[0]))
    print("")
    for i in range(len(predicted_cuisine)):
        if not (predicted_cuisine[i] == 0.0):
            print("The ingredients resemble %s with %f percentage" % (predicted_class[i], predicted_cuisine[i] * 100))

    print("")
    print("The %d closest meals are listed below : " % neighbors)
    match_perc, match_id = close.kneighbors(test_set)
    # print(df.head())
    for i in range(len(match_id[0])):
        id = meal_id[match_id[0][i]]
        # print(type(id))
        # print(id)
        # print(df.index.name)
        # print(df.iloc["id"]["style"])
        # if df.loc([id,'style']) == pref:
        print(meal_id[match_id[0][i]])
        # print(ingredients[match_id[0][i]])
    print("")

    print("--- It took %s seconds ---" % (time.time() - start_time))
    print("")
    print("")

    return predicted_single_cuisine


# main_func() function handles the sequential execution of the knn trainer and predictor
def main_func():
    user_ing = input("Enter the pantry availability : ")
    main_dataset = ing_vector(ingre, user_ing)
    train_set = main_dataset[:len(main_dataset) - 1]
    test_set = main_dataset[len(main_dataset) - 1]
    neighbors = input("Enter the number of closest recipes you want to find : ")
    pref = input("Enter your preferred cooking style:")
    time = input("Enter the time limit you have for cooking:")
    nutri = input("Preferred nutrition level(low,medium,high):")
    close = KNN_trainer(train_set, cuisine, neighbors)
    print("Model has been successfully trained..")
    print("Trying to predict the cuisine and n closest recipes...")
    KNN_predictor(test_set, close, neighbors)
    ingre.pop()
    try:
        nextStep = int(input("Enter 1 if you want to search again or 2 if you want to quit.."))
        if not (nextStep == 1 or nextStep == 2):
            raise ValueError()
        elif (nextStep == 1):
            main_func()
        elif (nextStep == 2):
            quit()
    except ValueError:
        print("Invalid Option. Enter correctly")
        main_func()


if __name__ == '__main__':
    print("Reading all the data files....")
    lists(filename="data files/data.json")
    df = pd.read_json('./data files/data.json')
    main_func()
