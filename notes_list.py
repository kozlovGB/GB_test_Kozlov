import csv
def notes_list():
    r = csv.reader(open('example.csv'))
    lines = list(r)
    print(lines)


