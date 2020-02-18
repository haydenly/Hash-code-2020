import csv

def hello():
    print("hello")

def load_data(f):
    r = csv.reader(f, delimiter = " ")
    data = []
    for row in r:
        data.append(list(map(int,row)))
    return (data[0],data[1:][0])

def main(fname):
    f = open(fname, "r+")
    params, data = load_data(f)
    print(params)
    print(data)

main("a_example.in")
