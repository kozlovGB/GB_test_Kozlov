import csv
def notes_dateSelect():
    date = input("Введите пожалуйста дату заметок, которые вы хотите увидеть: ")
    r = csv.reader(open('example.csv'))
    lines = list(r)
    delete_elements=[]
    for index in range(len(lines)):
        if lines[index] == []:
            delete_elements.append(index)
    if delete_elements!=[]:
        i = 0;
        for index in delete_elements:
            lines.pop(index-i)
            i+=1

    for index in range(len(lines)):
        if lines[index][2] == (date):
            print(lines[index])


