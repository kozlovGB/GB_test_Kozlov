import csv
import time

def notes_addContinue():
    with open('example.csv', 'a') as csvfile:
        title = input("Введите пожалуйста заголовок: ")
        content = input("Напишите заметку: ")
        time_string = time.strftime("%m/%d/%Y", time.localtime(time.time()))
        fieldnam = ['title', 'content', 'date']
        writer = csv.DictWriter(csvfile,  fieldnam)
        writer.writerow({'title': title , 'content': content , 'date': time_string })
    print("Writing complete")

