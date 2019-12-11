
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
        list_tmp = [float(num) for num in line[:-1]]
        list_tmp.append(line[-1])
        data.append(list_tmp)
    return data

