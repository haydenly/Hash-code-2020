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
        libs.append([libs_raw[2*i],libs_raw[2*i+1]])
    return (params, bookscores, libs)

def out_data(fname, scannedbooks):
    o = open(fname, "w")
    w = csv.writer(o, delimiter=" ", lineterminator="\n")
    m = len(scannedbooks)
    w.writerow([m])
    for i in range(m):
        curr_lib = scannedbooks[i]
        curr_books = curr_lib[1:]
        w.writerow([curr_lib[0],len(curr_books)])
        w.writerow(curr_books)
    o.close()
