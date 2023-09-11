import Notes.main2 as note2
import Notes.main as note
import Sorter.sorter as sorter

STOP_COMMAND = ["exit"]
MAIN_MENU = ["1", "2", "3", "4"]
PHONE_BOOK_MENU = ["1", "2", "3", "0"]
NOTES_MENU = ["1", "2", "3", "0"]



def input_error(func):
    def inner(*args, **kwargs):
        print('''Вас вітає, Almost_iPhone! 
        
<<<<<<< Updated upstream
        Я можу вам допомогти організувати ваші контакти за допомогою "Книгу контактів"
        або зберегти будь яку інформацію в "Нотатки",
        якщо у Вас є папка в котрій необхідно навести порядок - скристуйтесь "Сортувальником",
        якщо стало нудно - пограйте в гру "Бандеро Гусь",
        можливо скоро в меня зʼявляться інші функції...''')
        while True:
            print(''' 
            --  Введіть "1" - Ви відкриєте додаток "Книга контактів"
            --  Введіть "2" - Ви відкриєте додаток "Нотатки"
            --  Введіть "3" - Ви відкриєте додаток "Сортировальик"
            --  Введіть "4" - Ви зможете насолодись грою "Бандеро Гусь"
            --  Введіть "exit" - І я завершу свою роботу
            ''')
=======
    Я могу вам помочь организовать свои контакты с помощью "PHONE_BOOK"
    или сохранить любую информацию в "Заметки",
    если у вас есть папка в которой необходимо навести порядок - воспользуйтесь "Сортровщиком файлов",
    если стало скучно - поиграйте в игру "Бандеро Гусь",
    возможно скоро у меня появятся и другие функции...''')
        while True:
            print(''' 
        --  Введите "1" - Вы откроете "PHONE_BOOK"
        --  Введите "2" - Вы откроете "Заметки"
        --  Введите "3" - Вы откроете "Сортировщик файлов"
        --  Введите "4" - Вы откроете игру "Бандеро Гусь"
        --  Введите "exit" - И я завершу свою работу
        ''')
>>>>>>> Stashed changes
            try:
                result = func()
            except SystemExit:
                break
            except Exception as e:
                print("Error:", e)

    return inner


@input_error
def main():
    result = input("Введіть цифру и я запущу відповідний додаток: ")
    if len(result) == 0:
        print("Ви нічого не ввели, спробуйте ввести цифру.")

    elif result in STOP_COMMAND:
        print("Повертайтеся пізніше, я зможу допомогти Вам!")
        raise SystemExit

    elif not result.isnumeric():
        print("Ви ввели не додатне число, введіть одну цифру!")

    elif result in MAIN_MENU:
        if result == "1":
            print(result)
        elif result == "2":
            try:
                note.main_1()
            except:
                print(Exception.args[0])
        #Пример подменю ===========================
        elif result == "3":
<<<<<<< Updated upstream
            print('''
            Вас приветствует приложение "Заметки"
            Вы можете воспользоваться следующими функциями:
            --  Введите "1" - Для создания новой заметки
            --  Введите "2" - Для поиска заметок по [TAGS]
            --  Введите "3" - Для вывода всех сохраненных заметок
            --  Введите "0" - Для возвращения в Основное меню
            ''')
            while True:
                menu_3 = input("Введите номер функции: ")
                if menu_3 in NOTES_MENU:
                    if menu_3 == '0':
                        break
                    elif menu_3 == '1':
                        try:
                            note2.number_one("Hello")
                            continue
                        except:
                            print(Exception.args[0])
                    elif menu_3 == '2':
                        try:
                            note2.number_two("World")
                        except:
                            print(Exception.args[0])
                    elif menu_3 == '3':
                        try:
                            note.main_1()
                        except:
                            print(Exception.args[0])
                else:
                    print("Введите число 1, 2, 3, 4 или 0")
=======
            try:
                sorter.run()
            except:
                print(Exception.args[0])
>>>>>>> Stashed changes
        elif result == "4":
            try:
                import Game.game
            except:
                print(Exception)
        else:
            print("Oops...")

    else:
        print("У Вас вийде, спробуйте ввести цифру від 1 до 4 включно")

main()

print("OK")
