# Program with python
# Authors: Bartosz Pacia, Jakub Szafraniak, Grzegorz Musiał

import numpy as np
from math import sqrt


# function to get unique values
def unique(list1):
    x = np.array(list1)
    return np.unique(x)


def load_data_from_file(file):
    data = open(file, "r").read()
    data = data.split('\n')
    return data


def convert_to_float(data):
    data_tmp = []
    for line in data:
        data_tmp.append(line.split(","))
    data = []
    for line in data_tmp:
        list_tmp = [float(num) for num in line[1:-1]]
        list_tmp.append(line[-1])
        data.append(list_tmp)
    return data


# Append only last column
def only_last_column_append(data):
    tmp = []
    for line in data:
        tmp.append(line[-1])
    return tmp


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


# -------------------Configurations-------------------

# K neares neighbours
K = input("Value K: ")
K = int(K, 10)

# New data
new_object = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0]

# -------------------End configurations-------------------


# Load data from file and convert numbers to float
data = load_data_from_file("zoo.txt")
data = convert_to_float(data)

# Show decision class
classes = only_last_column_append(data)
print("\nClasses object in file:")
classes = unique(classes)
print(classes)

# Only vector explanatory designs
data_only_vector = []
for line in data:
    data_only_vector.append(line[:-1])

# Find nearest neighbors
nearest_objects = get_neighbors(data_only_vector, new_object, K)

# Show objects - find neares neighbors (portion information)
print("\nObject found(only vector):")
for line in nearest_objects:
    print(line)

# Find full object
near_full_obj = []
for line in nearest_objects:
    index = data_only_vector.index(line)
    near_full_obj.append(data[index])

# Show full objects
print("\nShow ful information object:")
for line in near_full_obj:
    print(line)

only_classes = []
for line in near_full_obj:
    only_classes.append(line[-1])

print("\nNew object:", new_object)
print("Class new object: ", max(only_classes, key=only_classes.count))