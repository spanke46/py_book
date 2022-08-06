# импортируем нужные библиотеки
import pyautogui as pg
import keyboard

# определим пустой список
list_services = []

# открываем файл
with open(u'c:\\py\services.txt','r') as file_object:
    for line in file_object:
        #удалим заключительный символ перехода строки
        currentPlace = line[:-1]
        # добавим элемент в конец списка
        list_services.append(currentPlace)

def write():
    # находим позицию курсора
    position = (pg.position())
    for code in list_services:
        pg.leftClick(position)
        pg.typewrite(str(code))
        pg.typewrite(['enter'])
        pg.PAUSE = 1

        # находим координаты названия услуги
        name_service = (pg.locateCenterOnScreen(r"C:\py\name_service.png"))
        if name_service == None:
            print(f' не нашло название услуги ')
            break

        # перемещаемся к нужной колонке с задержкой
        pg.moveTo(name_service, duration=0.02)
        # перемещаемся к первой услуге в списке
        pg.move(0, 25, duration=0.02)
        # 2 раза кликаем на услугу
        pg.click(clicks=2)
        pg.PAUSE = 1

        # находим позицию кнопки добавить
        p_add = (pg.locateCenterOnScreen(r"C:\py\add2.png"))
        if p_add == None:
            print(f' не нашло кнопку добавить , {name_service}')

        # нажимаем на кнопку
        pg.leftClick(p_add)
        # паузе между выполнением
        pg.PAUSE = 0.1

# хот кей на запуск функции
keyboard.add_hotkey('Alt + x', write)
# без этого не работает =)
keyboard.wait('Ctrl + Q')





