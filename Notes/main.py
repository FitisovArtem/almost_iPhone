from collections import UserDict
from datetime import datetime
# import json
import pickle
from pathlib import Path
from time import sleep

class Note:
    """
    Класс Note использует для обработки текста и тегов к
    тексту для дальнейшей записи в заметки.

    """

    def __init__(self, content: str, tags: str): # Инициализация текста заметки и тега для дальнейшей обработки
        self.content = content
        self.tags = tags.split(',')
        self.tags = sorted(self.tags)
        self.date = datetime.now().strftime('%d/%m/%Y %H:%M')


class NotesManager(UserDict):
    file_name = 'my_notes.bin'
    path_file_name = Path(file_name)

    def save_notes(self):
        with open(self.file_name, 'wb') as file:
            pickle.dump(self.data, file)

    def load_notes(self):
        if not self.path_file_name.exists():
            return print("File is empty")
        with open(self.file_name, 'rb') as file:
            self.data = pickle.load(file)

    def add_note(self, note: Note):
        self.data[len(self.data) + 1] = note

    def delete_note(self, chosen_id):
        del self.data[chosen_id]
        # if chosen_id < len(self.data):
        for i in range(int(chosen_id), len(self.data) + 1):
            self.data[i] = self.data[i + 1]
            del self.data[i + 1]

    def search_note(self, tag_for_search):
        title_of_result = f'Результаты поиска по запросу "{tag_for_search}" : \n'
        result = '\n'
        if tag_for_search is not None:
            for search_id, content_set in self.data.items():
                if tag_for_search in content_set.tags or tag_for_search in content_set.content:
                    result = result + f'{search_id}: {content_set.content}\n'
            if len(result) > 2:
                print(title_of_result)
                print(result)
            else:
                print('\n По Вашему запросу не найдено совпадений в заметка')
                sleep(1)
                return '0 result'

    def sorted_notes(self):
        dict_sorted = {}
        result = ''
        for chat_id, notes_class in self.data.items():
            dict_sorted[notes_class.date] = [chat_id,notes_class.content]
        a_dict = dict(sorted(dict_sorted.items()))
        for dict_1, in_dict in a_dict.items():
            result = result + f'{dict_1} : {in_dict[1]} : ID - {in_dict[0]}\n'
        return result
        # if type_of_sort == "A":
            # print(self.data[1].tags)
            # sortedDictWithValues = dict(sorted(self.data.items(), key=tags))
            # print(sortedDictWithValues)

    def edit_note(self, new_content, chosen_id_for_edit):
        self.data[chosen_id_for_edit].content = new_content

    def show_note(self,chosen_id):
        print(self.data[chosen_id].content)

    def __str__(self):
        if len(self.data) > 0:
            output = '{:>10}:  {:^15} | {:^20} | {:>10}\n'.format('["ID"]', '["TAGS"]', '["NOTE"]','[DATE]')
            for id_number, show_content in self.data.items():
                output = output + '{:>10}:  {:^15} | {:<20} | {:>10} \n'.format(id_number,','.join(show_content.tags)[:10] + "...", show_content.content[:17] + '...', show_content.date)
            return output
        else:
            return "Your notes book is empty"


def search_notes(notesBook: NotesManager):
    back_button = 'Для возврата в предыдущее меню введите 0'
    search_mark = True
    while search_mark:
        input_for_search = input('\nДля возврата в предыдущее меню введите 0\nВведите слово или текст которое хотите найти : ')
        if input_for_search == '':
            print('\n Запрос на поиск должен состоять минимум из слова или цифры')
            sleep(1)
            continue
        elif input_for_search == '0':
            break
        else:
            notesBook.search_note(input_for_search)
            while True:
                print('\n1 - Поиск по другому запросу \n0 - Для возврата в предыдущее меню')
                input_for_search_choice = input('\nВыберите действие')
                if input_for_search_choice not in ['1','0']:
                    print('\nВыберите действие из списка')
                    sleep(1)
                    continue
                elif input_for_search_choice == '1':
                    break
                else:
                    search_mark = False
                    break


def create_note(notesBook: NotesManager):
    back_button = '(Для возврата в предыдущее меню введите 0)'
    while True:
        input_note = input(f'\nВведите текст для заметки\n{back_button} : ')
        if input_note == '0':
            break
        else:
            if input_note.strip() != '':
                input_tag = input('Введите теги(через запятую)..по желанию: ')
                note = Note(input_note, input_tag)
                notesBook.add_note(note)
                print('\nЗапись добавлена')
                sleep(2)
                break
            else:
                print('\nЗаметка должна содержать хотя бы один символ. Повторите ввод')
                sleep(3)

def show_sorted_notes(notesBook: NotesManager):
    pass

def show_all_notes(notesBook: NotesManager):
    note_menu_2 = '1 - создать запись  2 - открыть запись\n3 - редактировать запись  4 - удалить запись\n5 - поиск  6 - сортировка по дате ↑\n0 - вернуться в предыдущее меню'
    type_show = 'A'
    while True:
        if type_show == 'A':
            print(notesBook)
            print(note_menu_2)
            input_todo_func = input('\nВыберите действие из списка выше')
            if input_todo_func not in ['1', '2', '3', '4', '0','5','6']:
                print('\n Ошибка ввода, повторите ваш выбор')
                sleep(2)
                continue
            elif input_todo_func == '1':
                create_note(notesBook)
            elif input_todo_func == '2':
                show_note(notesBook)
            elif input_todo_func == '3':
                edit_mode_note(notesBook)
            elif input_todo_func == '4':
                delete_note(notesBook)
            elif input_todo_func == '5':
                search_notes(notesBook)
            elif input_todo_func == '6':
                notesBook.sorted_notes()
                type_show = 'B'
                continue
            elif input_todo_func == '0':
                break
        else:
            print(notesBook.sorted_notes())
            print(note_menu_2)
            input_todo_func = input('\nВыберите действие из списка выше')
            if input_todo_func not in ['1', '2', '3', '4', '0', '5', '6']:
                print('\n Ошибка ввода, повторите ваш выбор')
                sleep(2)
                continue
            elif input_todo_func == '1':
                create_note(notesBook)
            elif input_todo_func == '2':
                show_note(notesBook)
            elif input_todo_func == '3':
                edit_mode_note(notesBook)
            elif input_todo_func == '4':
                delete_note(notesBook)
            elif input_todo_func == '5':
                search_notes(notesBook)
            elif input_todo_func == '6':
                notesBook.sorted_notes()
                type_show = 'A'
                continue
            elif input_todo_func == '0':
                break


def show_note(notesBook: NotesManager):
    note_menu_3 = '1 - редактировать запись\n2 - удалить запись\n0-вернуться назад : '
    while True:
        input_chat_id = input("\nВведите номер заметки : ")
        if input_chat_id == '0':
            break
        else:
            try:
                notesBook.show_note(int(input_chat_id))
            except:
                print('\nПовторите ввод')
                continue
            while True:
                ink = input(note_menu_3)
                if ink not in ['1', '2', '0']:
                    print('\nВыберите правильное действие')
                    sleep(1)
                elif ink == '1':
                    edit_note(notesBook, input_chat_id)
                elif ink == '2':
                    notesBook.delete_note(int(input_chat_id))
                    print('\nЗапись удалена ')
                    sleep(1)
                    break
                elif ink == '0':
                    break
            break


def edit_mode_note(notesBook:NotesManager):
    while True:
        input_chose_id_for_edit = input(
            '\nДля возрата назад введите 0\nВведите номер записи которую хотите редактировать : ')
        if input_chose_id_for_edit != '0':
            try:
                notesBook.data[int(input_chose_id_for_edit)]
            except:
                print('Введите коректный айди заметки')
                sleep(1)
                continue
            edit_note(notesBook,input_chose_id_for_edit)
            break
        else:
            break


def edit_note(notesBook: NotesManager, input_chose_id_for_edit):
    while True:
        input_content_for_edit = input(' \nВведите новый текст заметки :')
        if input_content_for_edit == '':
            print('\nЗаметка не может быть пустой')
            sleep(1)
            continue
        else:
            notesBook.edit_note(input_content_for_edit, int(input_chose_id_for_edit))
            print('\nЗаметка изменена и сохранина')
            sleep(1)
            edit_mode = False
            break


def delete_note(notesBook: NotesManager):
    while True:
        input_chat_id_for_delete = input("\nВведите номер заметки : ")
        if input_chat_id_for_delete != '0':
            try:
                notesBook.delete_note(int(input_chat_id_for_delete))

            except:
                print('\nПовторите ввод')

            print('\nЗапись удалена ')
            sleep(1)
            break
        else:
            break


def main_1():
    note_menu_1 = '1 - создать запись\n2 - показать все записи\n0 - выйти из приложения Заметки'
    notesBook = NotesManager()
    notesBook.load_notes()
    while True:
        print("\nНотатки")
        print(note_menu_1)
        first_choose = input('Выберите действие: ')
        if first_choose == '1':
            create_note(notesBook)

        elif first_choose == '2':
            show_all_notes(notesBook)
        elif first_choose == '3':
            notesBook.sorted_notes()
        elif first_choose == '0':
            notesBook.save_notes()
            print('Bye')
            sleep(2)
            break
        else:
            print('Ошибка выбора, повторите попытку')
            sleep(2)


if __name__ == "__main__":
    main_1()


class Note:
    """
    Класс Note использует для обработки текста и тегов к
    тексту для дальнейшей записи в заметки.
    """


    def __init__(self, content: str, tags: str): # Инициализация текста заметки и тега для дальнейшей обработки
        self.content = content
        self.tags = tags.split(',')
        self.tags = sorted(self.tags)
        self.date = datetime.now().strftime('%d/%m/%Y %H:%M')


class NotesManager(UserDict):
    file_name = 'Notes/my_notes.bin'
    path_file_name = Path(file_name)

    def save_notes(self):
        with open(self.path_file_name, 'wb') as file:
            pickle.dump(self.data, file)

    def load_notes(self):
        if not self.path_file_name.exists():
            return print("File is empty")
        with open(self.path_file_name, 'rb') as file:
            self.data = pickle.load(file)

    def add_note(self, note: Note):
        self.data[len(self.data) + 1] = note

    def delete_note(self, chosen_id):
        del self.data[chosen_id]
        # if chosen_id < len(self.data):
        for i in range(int(chosen_id), len(self.data) + 1):
            self.data[i] = self.data[i + 1]
            del self.data[i + 1]

    def search_note(self, tag_for_search):
        title_of_result = f'Результаты поиска по запросу "{tag_for_search}" : \n'
        result = '\n'
        if tag_for_search is not None:
            for search_id, content_set in self.data.items():
                if tag_for_search in content_set.tags or tag_for_search in content_set.content:
                    result = result + f'{search_id}: {content_set.content}\n'
            if len(result) > 2:
                print(title_of_result)
                print(result)
            else:
                print('\n По Вашему запросу не найдено совпадений в заметка')
                sleep(1)
                return '0 result'

    def sorted_notes(self):
        dict_sorted = {}
        result = ''
        for chat_id, notes_class in self.data.items():
            dict_sorted[notes_class.date] = [chat_id,notes_class.content]
        a_dict = dict(sorted(dict_sorted.items()))
        for dict_1, in_dict in a_dict.items():
            result = result + f'{dict_1} : {in_dict[1]} : ID - {in_dict[0]}\n'
        return result
        # if type_of_sort == "A":
            # print(self.data[1].tags)
            # sortedDictWithValues = dict(sorted(self.data.items(), key=tags))
            # print(sortedDictWithValues)

    def edit_note(self, new_content, chosen_id_for_edit):
        self.data[chosen_id_for_edit].content = new_content

    def show_note(self,chosen_id):
        print(self.data[chosen_id].content)

    def __str__(self):
        if len(self.data) > 0:
            output = '{:>10}:  {:^15} | {:^20} | {:>10}\n'.format('["ID"]', '["TAGS"]', '["NOTE"]','[DATE]')
            for id_number, show_content in self.data.items():
                output = output + '{:>10}:  {:^15} | {:<20} | {:>10} \n'.format(id_number,','.join(show_content.tags)[:10] + "...", show_content.content[:17] + '...', show_content.date)
            return output
        else:
            return "Your notes book is empty"


def search_notes(notesBook: NotesManager):
    back_button = 'Для возврата в предыдущее меню введите 0'
    search_mark = True
    while search_mark:
        input_for_search = input('\nДля возврата в предыдущее меню введите 0\nВведите слово или текст которое хотите найти : ')
        if input_for_search == '':
            print('\n Запрос на поиск должен состоять минимум из слова или цифры')
            sleep(1)
            continue
        elif input_for_search == '0':
            break
        else:
            notesBook.search_note(input_for_search)
            while True:
                print('\n1 - Поиск по другому запросу \n0 - Для возврата в предыдущее меню')
                input_for_search_choice = input('\nВыберите действие')
                if input_for_search_choice not in ['1','0']:
                    print('\nВыберите действие из списка')
                    sleep(1)
                    continue
                elif input_for_search_choice == '1':
                    break
                else:
                    search_mark = False
                    break


def create_note(notesBook: NotesManager):
    back_button = '(Для возврата в предыдущее меню введите 0)'
    while True:
        input_note = input(f'\nВведите текст для заметки\n{back_button} : ')
        if input_note == '0':
            break
        else:
            if input_note.strip() != '':
                input_tag = input('Введите теги(через запятую)..по желанию: ')
                note = Note(input_note, input_tag)
                notesBook.add_note(note)
                print('\nЗапись добавлена')
                sleep(2)
                break
            else:
                print('\nЗаметка должна содержать хотя бы один символ. Повторите ввод')
                sleep(3)

def show_sorted_notes(notesBook: NotesManager):
    pass

def show_all_notes(notesBook: NotesManager):
    note_menu_2 = '1 - создать запись  2 - открыть запись\n3 - редактировать запись  4 - удалить запись\n5 - поиск  6 - сортировка по дате ↑\n0 - вернуться в предыдущее меню'
    type_show = 'A'
    while True:
        if type_show == 'A':
            print(notesBook)
            print(note_menu_2)
            input_todo_func = input('\nВыберите действие из списка выше')
            if input_todo_func not in ['1', '2', '3', '4', '0','5','6']:
                print('\n Ошибка ввода, повторите ваш выбор')
                sleep(2)
                continue
            elif input_todo_func == '1':
                create_note(notesBook)
            elif input_todo_func == '2':
                show_note(notesBook)
            elif input_todo_func == '3':
                edit_mode_note(notesBook)
            elif input_todo_func == '4':
                delete_note(notesBook)
            elif input_todo_func == '5':
                search_notes(notesBook)
            elif input_todo_func == '6':
                notesBook.sorted_notes()
                type_show = 'B'
                continue
            elif input_todo_func == '0':
                break
        else:
            print(notesBook.sorted_notes())
            print(note_menu_2)
            input_todo_func = input('\nВыберите действие из списка выше')
            if input_todo_func not in ['1', '2', '3', '4', '0', '5', '6']:
                print('\n Ошибка ввода, повторите ваш выбор')
                sleep(2)
                continue
            elif input_todo_func == '1':
                create_note(notesBook)
            elif input_todo_func == '2':
                show_note(notesBook)
            elif input_todo_func == '3':
                edit_mode_note(notesBook)
            elif input_todo_func == '4':
                delete_note(notesBook)
            elif input_todo_func == '5':
                search_notes(notesBook)
            elif input_todo_func == '6':
                notesBook.sorted_notes()
                type_show = 'A'
                continue
            elif input_todo_func == '0':
                break


def show_note(notesBook: NotesManager):
    note_menu_3 = '1 - редактировать запись\n2 - удалить запись\n0-вернуться назад : '
    while True:
        input_chat_id = input("\nВведите номер заметки : ")
        if input_chat_id == '0':
            break
        else:
            try:
                notesBook.show_note(int(input_chat_id))
            except:
                print('\nПовторите ввод')
                continue
            while True:
                ink = input(note_menu_3)
                if ink not in ['1', '2', '0']:
                    print('\nВыберите правильное действие')
                    sleep(1)
                elif ink == '1':
                    edit_note(notesBook, input_chat_id)
                elif ink == '2':
                    notesBook.delete_note(int(input_chat_id))
                    print('\nЗапись удалена ')
                    sleep(1)
                    break
                elif ink == '0':
                    break
            break


def edit_mode_note(notesBook:NotesManager):
    while True:
        input_chose_id_for_edit = input(
            '\nДля возрата назад введите 0\nВведите номер записи которую хотите редактировать : ')
        if input_chose_id_for_edit != '0':
            try:
                notesBook.data[int(input_chose_id_for_edit)]
            except:
                print('Введите коректный айди заметки')
                sleep(1)
                continue
            edit_note(notesBook,input_chose_id_for_edit)
            break
        else:
            break


def edit_note(notesBook: NotesManager, input_chose_id_for_edit):
    while True:
        input_content_for_edit = input(' \nВведите новый текст заметки :')
        if input_content_for_edit == '':
            print('\nЗаметка не может быть пустой')
            sleep(1)
            continue
        else:
            notesBook.edit_note(input_content_for_edit, int(input_chose_id_for_edit))
            print('\nЗаметка изменена и сохранина')
            sleep(1)
            edit_mode = False
            break


def delete_note(notesBook: NotesManager):
    while True:
        input_chat_id_for_delete = input("\nВведите номер заметки : ")
        if input_chat_id_for_delete != '0':
            try:
                notesBook.delete_note(int(input_chat_id_for_delete))

            except:
                print('\nПовторите ввод')

            print('\nЗапись удалена ')
            sleep(1)
            break
        else:
            break


def main_1():
    note_menu_1 = '1 - создать запись\n2 - показать все записи\n0 - выйти из приложения Заметки'
    notesBook = NotesManager()
    notesBook.load_notes()
    while True:
        print("\nНотатки")
        print(note_menu_1)
        first_choose = input('Выберите действие: ')
        if first_choose == '1':
            create_note(notesBook)

        elif first_choose == '2':
            show_all_notes(notesBook)
        elif first_choose == '3':
            notesBook.sorted_notes()
        elif first_choose == '0':
            notesBook.save_notes()
            print('Bye')
            sleep(2)
            break
        else:
            print('Ошибка выбора, повторите попытку')
            sleep(2)


if __name__ == "__main__":
    main_1()
