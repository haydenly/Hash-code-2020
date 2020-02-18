import csv 

def load_data(fname):
    f = open(fname, mode="r")
    r = csv.reader(f, delimiter = " ")
    data = []
    for row in r:
        data.append(list(map(int,row)))
    f.close()
    return (data[0],data[1:])

def out_data(fname, rides):
    o = open(fname, "w")
    w = csv.writer(o, delimiter=" ", lineterminator="\n")
    for ride in rides:
        w.writerow(ride)
    o.close()
