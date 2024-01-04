import Note

def create_note(number):
    title = check_len_text_input(
        input('\n\033[35mВведите название заметки: \033[0m'), number)
    body = check_len_text_input(
        input('\n\033[35mВведите описание заметки: \033[0m'), number)
    return Note.Note(title=title, body=body)

def menu():
    print("\n\033[34mЭто программа 'Заметки'. Имеются следующие функции:\033[0m\n\n""\033[32m"+"1 - Вывод всех заметок из файла\n2 - Добавление новой заметки\n3 - Удаление заметки\n4 - Редактирование заметки\n5 - Выборка заметок по дате\n6 - Показать заметку по id \n7 - Выход\n\033[0m\nВведите номер функции: ")

def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'\n\033[35mТекст должен быть больше {n} символов\033[0m\n')
        text = input('\n\033[35mВведите тескт: \033[0m')
    else:
        return text

def goodbuy():
    print("\033[31m"+"Приходите к нам еще =). До новых встреч!")
