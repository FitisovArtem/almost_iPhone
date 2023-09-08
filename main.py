import Notes.main as note

STOP_COMMAND = ["exit"]
ACTION_COMMAND = ["1", "2", "3", "4"]


def input_error(func):
    def inner(*args, **kwargs):
        print('''Вас приветствует, Almost_iPhone! 
        
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
            try:
                result = func()
            except SystemExit:
                break
            except IndexError:
                print("Вы ввели неправильное имя или телефон попробуйте еще...")
            except Exception as e:
                print("Error:", e)

    return inner


@input_error
def main():
    result = input("Введите цифру и я запущу приложение: ")
    if len(result) == 0:
        print("Вы ничего не ввели, попробуйте ввести цифру...")

    elif result in STOP_COMMAND:
        print("Возвращайтесь позже, я смогу Вам помочь!")
        raise SystemExit

    elif not result.isnumeric():
        print("Вы ввели не положительное целое число, введите одну цифру!")

    elif result in ACTION_COMMAND:
        if result == "1":
            print(result)
        elif result == "2":
            print(result)
        #Пример подменю ===========================
        elif result == "3":
            while True:
                print('''
                Вас приветствует приложение "Заметки"
                Вы можете воспользоваться следующими функциями:
                --  Введите "1" - Для создания новой заметки
                --  Введите "2" - Для поиска заметок по [TAGS]
                --  Введите "3" - Для вывода всех сохраненных заметок
                --  Введите "0" - Для возвращения в Основное меню
                ''')
                menu_3 = input("Введите номер функции: ")
                if menu_3.isnumeric():
                    if menu_3 == '0':
                        break
                    elif menu_3 == '1':
                        try:
                            note.number_one("Hello")
                            continue
                        except:
                            print(Exception.args[0])
                    elif menu_3 == '2':
                        try:
                            note.number_two("World")
                        except:
                            print(Exception.args[0])
                    elif menu_3 == '3':
                        try:
                            note.number_three("Wow")
                        except:
                            print(Exception.args[0])
        elif result == "4":
            try:
                import Game.game
            except:
                print(Exception)
        else:
            print("Oops...")

    else:
        print("У Вас получится, попробуйте ввести цифру от 1 до 4 включительно")


main()
