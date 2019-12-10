'''
PROJEKT PYTHON
AUTORZY:
BARTOSZ PACIA
GRZEGORZ MUSIAL
JAKUB SZAFRANIAK
'''
from math import sqrt


# zaladuj plik z danymi i zapisz w postaci liczb zmiennoprzecinkowych
# implementacja parsera
def load_data(fname):
    f = open(fname,'r')
    line = f.readlines()
    line_new = []
    line_new1 = []
    for line1 in line:
        line_new = []
        line1 = line1.split(",")
        for line2 in line1:
            line_new.append(float(line2.strip()))
        line_new[-1] = int(line_new[-1])
        line_new1.append(line_new)
    return line_new1


#obliczanie odległości euklidesowej
def e_distance(row1, row2):
    dist = 0.0
    for i in range(len(row1)-1):
        dist = dist + (row1[i] - row2[i])**2
    sq_dist = sqrt(dist)
    return sq_dist


# sklasyfikuj
def predict(data, test_data, x_num):
    neighbors = find_neighbors(data, test_data, x_num)
    out = [row[-1] for row in neighbors]
    predict = max(set(out), key=out.count)
    return predict


#Znajdz "x_num" najblizszych sasiadow
def find_neighbors(data,test_data,x_num):
    dist = []
    for data_row in data:
        data2 = e_distance(test_data,data_row)
        dist.append((test_data, data2))
    dist.sort(key=lambda tup: tup[1])
    neighbors = []
    for j in range(x_num):
        neighbors.append(dist[j][0])
    return neighbors

# kNN Algorithm


ile = 5
data=load_data('tekst.txt')
#print(data)
test=[0.2,2.5,1.6,2.8,0]
neigh = predict(data,test,ile)
print(neigh)
