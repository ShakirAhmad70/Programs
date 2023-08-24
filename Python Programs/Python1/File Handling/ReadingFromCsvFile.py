import csv

with open("employee.csv", 'r') as f:
    r = csv.reader(f)
    # print(type(r))
    data = list(r)
    # print(data) #list of list form
    for row in data:
        for column in row:
            print(column,end='\t')
        print()
    