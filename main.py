from GB_test_Kozlov.notes_add import notes_add
from GB_test_Kozlov.notes_add2 import notes_addContinue
from GB_test_Kozlov.notes_dateSelect import notes_dateSelect
from GB_test_Kozlov.notes_delete import notes_delete
from GB_test_Kozlov.notes_edit import notes_edit
from GB_test_Kozlov.notes_list import notes_list

print("Добрый день, введите, пожалуйста команду для далььнейшей работы с заметками\n"
      "list - Вывод всех заметок\n"
      "add_New - создание нового файла для заметок (ЗАПИСЫВАТЬСЯ ТОЛЬКО ОДН РАЗ, ПРИ ДАЛЬНЕЙШЕМ ИСПОЛЬЗОВАНИИ БУДЕТ ПЕРЕЗАПИСЬ)\n"
      "add - создание новой заметки, в существующий файл\n"
      "dateSelect - сортировка по дате\n"
      "delete - удаление заметки по заголовку\n"
      "edit - редактирование заметки\n"
      )
command = input("Введите пожалуйста команду: ")

match command:
    case "list":
        notes_list()
    case "add_New":
        notes_add()
    case "add":
        notes_addContinue()
    case "dateSelect":
        notes_dateSelect()
    case "delete":
        notes_delete()
    case "edit":
        notes_edit()
    case _:
        print("Warring: Неизвестная команда")



