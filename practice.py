import csv

def load_data(fname):
    f = open(fname, "r+")
    r = csv.reader(f, delimiter = " ")
    data = []
    for row in r:
        data.append(list(map(int,row)))
    f.close()
    return (data[0],data[1:][0])

def out_data(chosenPizzas, fname):
    o = open(fname, "w")
    w = csv.writer(o, delimiter=" ", lineterminator="\n")
    w.writerow([len(chosenPizzas)])
    w.writerow(chosenPizzas)
    o.close()

def main(fname):
    params, data = load_data(fname)
    print(params)
    print(data)

main("a_example.in")
