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

def out_data(fname, order, scannedbooks):
    o = open(fname, "w")
    w = csv.writer(o, delimiter=" ", lineterminator="\n")
    m = scannedbooks.length()
    w.writerow(m)
    for i in range(m):
        n = scannedbooks[i].length()
        w.write(i)
        w.write(n)
        w.writerow(scannedbooks[i])
    o.close()
