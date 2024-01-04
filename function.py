import file_operation
import Note
import ui

number = 6  # сколько знаков МИНИМУМ может быть в тексте заметки

def add():
    note = ui.create_note(number)
    array = file_operation.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    file_operation.write_file(array, 'a')
    print('\n\033[35mЗаметка добавлена...\033[0m')

def show(text):
    logic = True
    array = file_operation.read_file()
    if text == 'date':
        date = input('\n\033[35mВведите дату в формате dd.mm.yyyy: \033[0m')
    for notes in array:
        if text == 'all':
            logic = False
            print(Note.Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + Note.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in Note.Note.get_date(notes):
                print(Note.Note.map_note(notes))
    if logic == True:
        print('Нет ни одной заметки...\033[0m')

def id_edit_del_show(text):
    id = input('Введите id необходимой заметки: \033[0m')
    array = file_operation.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = ui.create_note(number)
                Note.Note.set_title(notes, note.get_title())
                Note.Note.set_body(notes, note.get_body())
                Note.Note.set_date(notes)
                print('\n\033[35mЗаметка изменена...\033[0m')
            if text == 'del':
                array.remove(notes)
                print('\n\033[35mЗаметка удалена...\033[0m')
            if text == 'show':
                print(Note.Note.map_note(notes))
    if logic == True:
        print('\n\033[35mТакой заметки нет, возможно, вы ввели неверный id\033[0m')
    file_operation.write_file(array, 'a')
