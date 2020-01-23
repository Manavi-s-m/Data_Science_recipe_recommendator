import knn
import random
import numpy as np
import time

start_time = time.time()

per_test = []
per_test_id = []
per_train = []
per_train_id = []
per_train_cuisine = []
per_test_cuisine = []

print("started")
knn.lists(filename="./data files/data.json")
full_list = knn.ing_vector(knn.ing, "\'onion\' \'carrot\' \'celery\' \'solid pack pumpkin\' \'red bell pepper\'")
print("list completed")

train_list = np.array(full_list)

for i in range(0, len(full_list) - 1):
    if random.random() < 0.95:
        per_train.append(train_list[i])
        per_train_id.append(knn.meal_id[i])
        per_train_cuisine.append(knn.cuisine[i])
    else:
        per_test.append(full_list[i])
        per_test_id.append(knn.meal_id[i])
        per_test_cuisine.append(knn.cuisine[i])

print("Training is starting..")
per_close_n = knn.KNN_trainer(per_train, per_train_cuisine, 5)

print("Training completed")
no_of_tests = len(per_test)
no_of_passes = 0

print("Testing is starting..")
print(no_of_tests)
cuisine = ['indian', 'mexican', 'chinese', 'thai', 'italian', 'american', 'asian', 'middle-eastern', 'hawaiian',
           'european', 'north-american']
arr = np.zeros(shape=(22, 2))
for i in range(0, len(per_test)):
    print(i)
    per_cuisine = knn.KNN_predictor(per_test[i], per_close_n, 5)
    if per_cuisine not in cuisine:
        print(per_cuisine)
        break
    if per_test_cuisine[i] not in cuisine:
        print(per_test_cuisine[i])
        break
    print(per_cuisine, per_test_cuisine[i])
    pred_cus = per_cuisine
    actual_cus = per_test_cuisine[i]
    pred_pos = cuisine.index(per_cuisine)
    actual_pos = cuisine.index(per_test_cuisine[i])
    if actual_cus == pred_cus:
        arr[actual_pos*2][0] =arr[actual_pos*2][0] + 1
        no_of_passes += 1
    elif pred_cus != actual_cus:
        arr[pred_pos*2][1] = arr[pred_pos*2][1] + 1
        arr[actual_pos*2 + 1][0] = arr[actual_pos*2 + 1][0] + 1
    for j in range(0, 11):
        if j != actual_pos and j != pred_pos:
            arr[j*2 + 1][1] = arr[j*2 + 1][1] + 1

arr = arr * 1 / no_of_tests

final = np.zeros(shape=(2, 2))
for j in range(0, 11):
    final[0][0] += arr[j][0]
    final[0][1] += arr[j][1]
    final[1][0] += arr[j+1][0]
    final[1][1] += arr[j+1][1]

final = final*1/11

print("--- It took %s seconds ---" % (time.time() - start_time))

print("Accuracy percentage %d" % ((no_of_passes / no_of_tests) * 100))
