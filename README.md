# Data-Science-Project

In this project, a recommendation system has been built and tested for providing a user with recipes to cook based on his/her pantry availability and cooking preferences. A machine learning approach was used to build the system. The dataset which was used to build the recommendation system consisted of user ratings for recipes, cuisines, ingredients and instructions to be followed in the recipe, etc. This dataset was cleaned to ensure better and more accurate predictions. Cleaning also involved obtaining the cuisine and method of cooking involved. Then, a K-Nearest Neighbors algorithm (KNN) was trained on the dataset with target feature as the cuisine and the ingredients as the input features. Then, when a user inputs his/her pantry and cooking method preferred, the trained model is used to predict a cuisine and then using the cuisine, a set of recipes are recommended based on the user preference. The model was tested using K-fold cross validation and found to be about 75% accurate in predicting the cuisine.

Dataset link : https://www.kaggle.com/shuyangli94/food-com-recipes-and-user-interactions
IDE used : IntelliJ
Libraries used : Pandas, Numpy, Sklearn
