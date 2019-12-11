
# Program with python
#Authors: Bartosz Pacia, Jakub Szafraniak, Grzegorz Musiał

import numpy as np
from math import sqrt
from collections import Counter


# function to get unique values
def unique(list1):
    x = np.array(list1)
    return np.unique(x)

def load_data_from_file(file):
    data = open(file, "r").read()
    data = data.split('\n')
    data_tmp = []
    for line in data:
        data_tmp.append(line.split(","))
    data = []
    for line in data_tmp:
        list_tmp = [float(num) for num in line[:-1]]
        list_tmp.append(line[-1])
        data.append(list_tmp)
    return data


# Calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
    distance = 0.0
    for i in range(len(row1) - 1):
        distance += (row1[i] - row2[i]) ** 2
    return sqrt(distance)


def get_neighbors(train, test_row, num_neighbors):
    distances = list()
    for train_row in train:
        dist = euclidean_distance(test_row, train_row)
        distances.append((train_row, dist))
    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(num_neighbors):
        neighbors.append(distances[i][0])
    return neighbors

# Configurations

K = 5
NUM_COL_DATA = 3

new_object = [4.7,3.2,1.3,.2]

# Load data from file and convert numbers to float

data = load_data_from_file("file1.txt")

#print(data)

# Show classes decision
classes = []
for line in data:
    classes.append(line[-1])

print("\nClasses object in file:")
classes = unique(classes)
print(classes)

# Only vector explanatory designs
data_only_vector = []
for line in data:
    data_only_vector.append(line[:-1])

nearest_objects = get_neighbors(data_only_vector, new_object, K)

#show objects
print("\nShow object for only vector:")
for line in nearest_objects:
    print(line)

#find full object
near_full_obj = []
for line in nearest_objects:
    index = data_only_vector.index(line)
    near_full_obj.append(data[index])

#show objects
print("\nShow ful information object:")
for line in near_full_obj:
    print(line)

only_classes = []
for line in near_full_obj:
    only_classes.append(line[-1])


print(Counter(only_classes).keys() )# equals to list(set(words))
print(Counter(only_classes).values()) # counts the elements' frequency

