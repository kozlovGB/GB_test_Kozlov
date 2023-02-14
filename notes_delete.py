import csv
def notes_delete():
    title = input("Введите пожалуйста заголовок заметки, которую вы хотите удалить: ")
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
        if lines[index][0] == (title):
            lines.pop(index)
            break

    writer = csv.writer(open('example.csv', 'w'))
    writer.writerows(lines)

