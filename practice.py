import csv

def hello():
    print("hello")

def load_data(fname):
    f = open(fname, "r+")
    r = csv.reader(f, delimiter = " ")
    data = []
    for row in r:
        data.append(list(map(int,row)))
    f.close()
    return (data[0],data[1:][0])

def main(fname):
    params, data = load_data(fname)
    print(params)
    print(data)

main("a_example.in")
