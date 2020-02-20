import csv 

def load_data(fname):
    f = open(fname, mode="r")
    r = csv.reader(f, delimiter = " ")
    data = []
    for row in r:
        data.append(list(map(int,row)))
    f.close()
    params = data[0]
    bookscores = data[1]
    libs_raw = data [2:]
    libs = []
    for i in range(len(libs_raw)//2):
        libs.append([libs_raw[i],libs_raw[i+1]])
    return (params, bookscores, libs)

def out_data(fname, data):
    o = open(fname, "w")
    w = csv.writer(o, delimiter=" ", lineterminator="\n")
    for ride in rides:
        w.writerow(ride)
    o.close()
