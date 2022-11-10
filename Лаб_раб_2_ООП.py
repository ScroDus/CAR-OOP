#Создает соответствующие списки для параметров машинки и колличества этих параметров
Marks = []        #Марка
Body_Cars = []   #Кузов
Engines = []      #Двигатель
Colors = []       #Цвет
Transmissions = [] #Коробка передач
Door_1_L = []    #Передняя левая дверь
Door_1_R = []    #Передняя правая дверь
Door_2_L = []    #Задняя левая дверь
Door_2_R = []    #Задняя правая дверь
Headlights = []  #Фары


#Хранит колличество марок, цветов и т.д. в отдельном файле
Mark_S = []
Body_Cars_S = []
Engine_S = []
Color_S = []
Transmission_S = []
Doors_S = []
Headlights_S = []

class Mark:
    def Create_Mark(self, a):
        Marks.append(Mark_S[a-1])

    def Change_Mark(self, a, b):
        print(f'Текущай марка машинки:{Mark_S[a - 1]}')
        while True:
            b = int(input('Введите новую марку: '))
            if b >= 1 and b <= len(Mark_S):
                break
            else:
                print('Данные не корректны')
        Marks[a-1] = Mark_S[b-1]

    def Check_Mark(self):
        for i in range(len(Mark_S)):
            i1 = int(i+1)
            print(f"{i1}) {Mark_S[i]}")


class Body_Car:
    def Check_Body_Car(self):
        for i in range(len(Body_Cars_S)):
            i1 = int(i+1)
            print(f"{i1}) {Body_Cars_S[i]}")

    def Create_Body_Car(self, a):
        Body_Cars.append(Body_Cars_S[a-1])

    def Change_Body_Car(self, a, b):
        print(f'Текущий кузов машинки:{Body_Cars_S[a - 1]}')
        while True:
            b = int(input('Введите новый кузов: '))
            if b >= 1 and b <= len(Body_Cars_S):
                break
            else:
                print('Данные не корректны')
        Body_Cars[a-1] = Body_Cars_S[b-1]


class Engine:
    def Check_Engine(self):
        for i in range(len(Engine_S)):
            i1 = int(i+1)
            print(f"{i1}) {Engine_S[i]}")

    def Create_Engine(self, a):
        Engines.append(Engine_S[a-1])

    def Change_Engine(self, a, b):
        print(f'Текущий двигатель машинки:{Engine_S[a - 1]}')
        while True:
            b = int(input('Введите новый двигатель: '))
            if b >= 1 and b <= len(Engine_S):
                break
            else:
                print('Данные не корректны')
        Engines[a-1] = Engine_S[b-1]


class Color:
    def Check_Color(self):
        for i in range(len(Color_S)):
            i1 = int(i+1)
            print(f"{i1}) {Color_S[i]}")

    def Create_Color(self, a):
        Colors.append(Color_S[a-1])

    def Change_Color(self, a, b):
        print(f"Текущий цвет машинки:{Color_S[a - 1]}")
        while True:
            b = int(input('Введите новый цвет: '))
            if b >= 1 and b <= len(Color_S):
                break
            else:
                print('Данные не корректны')
        Colors[a-1] = Color_S[b-1]

class Transmission:
    def Check_Transmission(self):
        for i in range(len(Transmission_S)):
            i1 = int(i+1)
            print(f"{i1}) {Transmission_S[i]}")

    def Create_Transmission(self, a):
        Transmissions.append(Transmission_S[a-1])

    def Change_Transmission(self, a, b):
        print(f"Текущий цвет машинки:{Transmission_S[a - 1]}")
        while True:
            b = int(input('Введите новый цвет: '))
            if b >= 1 and b <= len(Transmission_S):
                break
            else:
                print('Данные не корректны')
        Transmissions[a-1] = Transmission_S[b-1]

class Doors:
    def Create_Door_1_L(self, Doors_S):
        Door_1_L.append(Doors_S[1])

    def Create_Door_1_R(self, Doors_S):
        Door_1_R.append(Doors_S[1])

    def Create_Door_2_L(self, Doors_S):
        Door_2_L.append(Doors_S[1])

    def Create_Door_2_R(self, Doors_S):
        Door_2_R.append(Doors_S[1])

    def Change_Doors(self, Doors_S):
        print('1) Передняя левая дверь')
        print('2) Передняя правая дверь')
        print('3) Задняя левая дверь')
        print('4) Задняя правая дверь')
        while True:
            b1 = int(input('Выберите дверь: '))
            if b1 >= 1 and b1 <= 4:
                break
            else:
                print('Данные не корректны')

        if b1 == 1:
            print('1) Открыть дверь')
            print('2) Закрыть дверь')
            print(f'Текущее положение двери:{Door_1_L[a - 1]}')
            while True:
                b2 = int(input('Выберите действие '))
                if b2 >= 1 and b2 <= 2:
                    break
                else:
                    print('Данные не корректны')
            if b2 == 1:
                Door_1_L[a-1] = Doors_S[0]
            if b2 == 2:
                Door_1_L[a-1] = Doors_S[1]

        if b1 == 2:
            print('1) Открыть дверь')
            print('2) Закрыть дверь')
            print(f'Текущее положение двери:{Door_1_R[a - 1]}')
            while True:
                b2 = int(input('Выберите действие '))
                if b2 >= 1 and b2 <= 2:
                    break
                else:
                    print('Данные не корректны')
            if b2 == 1:
                Door_1_R[a-1] = Doors_S[0]
            if b2 == 2:
                Door_1_R[a-1] = Doors_S[1]

        if b1 == 3:
            print('1) Открыть дверь')
            print('2) Закрыть дверь')
            print(f'Текущее положение двери:{Door_2_L[a - 1]}')
            while True:
                b2 = int(input('Выберите действие '))
                if b2 >= 1 and b2 <= 2:
                    break
                else:
                    print('Данные не корректны')
            if b2 == 1:
                Door_2_L[a-1] = Doors_S[0]
            if b2 == 2:
                Door_2_L[a-1] = Doors_S[1]

        if b1 == 4:
            print('1) Открыть дверь')
            print('2) Закрыть дверь')
            print(f'Текущее положение двери:{Door_2_R[a-1]}')
            while True:
                b2 = int(input('Выберите действие '))
                if b2 >= 1 and b2 <= 2:
                    break
                else:
                    print('Данные не корректны')
            if b2 == 1:
                Door_2_R[a-1] = Doors_S[0]
            if b2 == 2:
                Door_2_R[a-1] = Doors_S[1]

class Headlight:
    def Create_Headlights(self, Headlights_S):
        Headlights.append(Headlights_S[1])

    def Change_Headlights(self, Headlights_S):
        print('1) Включить фары')
        print('2) Выключить фары')
        print(f'Текущее положение фар:{Headlights[a-1]}')
        while True:
            b2 = int(input('Выберите действие '))
            if b2 >= 1 and b2 <= 2:
                break
            else:
                print('Данные не корректны')
        if b2 == 1:
            Headlights[a-1] = Headlights_S[0]
        if b2 == 2:
            Headlights[a-1] = Headlights_S[1]



class Car(Mark, Body_Car, Engine, Color, Doors, Headlight, Transmission):
    def __init__(self, mark, body_car, engine, color, door_1_L, door_1_R, door_2_L, door_2_R, headlights, marks, body_cars, engines, colors, transmission, transmissions):
        self.mark = Marks
        self.body_car = Body_Cars
        self.engine = Engines
        self.color = Colors
        self.door_1_L = Door_1_L
        self.door_1_R = Door_1_R
        self.door_2_L = Door_2_L
        self.door_2_R = Door_2_R
        self.headlights = Headlights
        self.marks = Mark_S
        self.body_cars = Body_Cars_S
        self.engines = Engine_S
        self.colors = Color_S
        self.transmission = Transmissions
        self.transmissions = Transmission_S

    def display_info(self):
        s4 = s1
        for i in range(s):
            i1 = int(i+1)
            k = 1
            for d in range(i):
                if Marks[d] == Marks[i]:
                    k += 1
            if s4 != 0 and s > 1 and i + 1 > s - s1:
                print('\n',end='')
                print(f"{i1}) Марка:{self.mark[i]}({k}) Кузов:{self.body_car[i]} Двигатель:{self.engine[i]} Коробка передач:{self.transmission[i]} Цвет:{self.color[i]} Двери: 1_Л:{self.door_1_L[i]} 1_R:{self.door_1_R[i]} 2_Л:{self.door_2_L[i]} 2_R:{self.door_2_R[i]} Фары:{self.headlights[i]}", end="")
                s4 = s4 - 1
            elif s > 1 and s3[i] == 1 and i != 0:
                print(f"{i1}) Марка:{self.mark[i]}({k}) Кузов:{self.body_car[i]} Двигатель:{self.engine[i]} Коробка передач:{self.transmission[i]} Цвет:{self.color[i]} Двери: 1_Л:{self.door_1_L[i]} 1_R:{self.door_1_R[i]} 2_Л:{self.door_2_L[i]} 2_R:{self.door_2_R[i]} Фары:{self.headlights[i]}", end="")
                print('\n', end='')
            else:
                print(f"{i1}) Марка:{self.mark[i]}({k}) Кузов:{self.body_car[i]} Двигатель:{self.engine[i]} Коробка передач:{self.transmission[i]} Цвет:{self.color[i]} Двери: 1_Л:{self.door_1_L[i]} 1_R:{self.door_1_R[i]} 2_Л:{self.door_2_L[i]} 2_R:{self.door_2_R[i]} Фары:{self.headlights[i]}", end="")


    def Delete(self, a):
            Marks.pop(a-1)
            Body_Cars.pop(a-1)
            Engines.pop(a-1)
            Transmissions.pop(a - 1)
            Colors.pop(a-1)
            Door_1_L.pop(a - 1)
            Door_1_R.pop(a - 1)
            Door_2_L.pop(a - 1)
            Door_2_R.pop(a - 1)
            Headlights.pop(a - 1)


    def Change_Characters(self):
            print('1) Марка')
            print('2) Кузов')
            print('3) Двигетель')
            print('4) Коробка передач')
            print('5) Цвет')
            b1 = int(input('Выберите параметр: '))

            if b1 == 1:
                print('1) Добавить марку')
                print('2) Удалить марку')
                b2 = int(input('Выберите действие: '))
                if b2 == 1:
                    b3 = input('Введите название новой марки: ')
                    Mark_S.append(b3)
                if b2 == 2 and len(Mark_S) > 1:
                    for i in range(len(Mark_S)):
                        i1 = int(i + 1)
                        print(f"{i1}) {Mark_S[i]}")
                    b3 = int(input('Выберите номер марки, которую хотите удалить: '))
                    Mark_S.pop(b3-1)

            if b1 == 2:
                print('1) Добавить кузов')
                print('2) Удалить кузов')
                b2 = int(input('Выберите действие: '))
                if b2 == 1:
                    b3 = input('Введите название нового кузова: ')
                    Body_Cars_S.append(b3)
                if b2 == 2 and len(Body_Cars_S) > 1:
                    for i in range(len(Body_Cars_S)):
                        i1 = int(i + 1)
                        print(f"{i1}) {Body_Cars_S[i]}")
                    b3 = int(input('Выберите номер кузова,который хотите удалить: '))
                    Body_Cars_S.pop(b3-1)

            if b1 == 3:
                print('1) Добавить двигатель')
                print('2) Удалить двигатель')
                b2 = int(input('Выберите действие: '))
                if b2 == 1:
                    b3 = input('Введите название нового двигателя: ')
                    Engine_S.append(b3)
                if b2 == 2 and len(Engine_S) > 1:
                    for i in range(len(Engine_S)):
                        i1 = int(i + 1)
                        print(f"{i1}) {Engine_S[i]}")
                    b3 = int(input('Выберите номер двигателя,который хотите удалить: '))
                    Engine_S.pop(b3-1)

            if b1 == 4:
                print('1) Добавить коробку передач')
                print('2) Удалить коробку передач')
                b2 = int(input('Выберите действие: '))
                if b2 == 1:
                    b3 = input('Введите название новой коробки передач: ')
                    Transmission_S.append(b3)
                if b2 == 2 and len(Transmission_S) > 1:
                    for i in range(len(Transmission_S)):
                        i1 = int(i + 1)
                        print(f"{i1}) {Transmission_S[i]}")
                    b3 = int(input('Выберите номер коробки передач,которую хотите удалить: '))
                    Transmission_S.pop(b3-1)

            if b1 == 5:
                print('1) Добавить цвет')
                print('2) Удалить цвет')
                b2 = int(input('Выберите действие: '))
                if b2 == 1:
                    b3 = input('Введите название нового цвета: ')
                    Color_S.append(b3)
                if b2 == 2 and len(Color_S) > 1:
                    for i in range(len(Color_S)):
                        i1 = int(i + 1)
                        print(f"{i1}) {Color_S[i]}")
                    b3 = int(input('Выберите номер цвета,который хотите удалить: '))
                    Color_S.pop(b3-1)



s = 0
s1 = 0
k = 1

h = open('Specifications.txt', 'r+', encoding='utf-8')
while k !=8:
    a = h.readline()
    a = a.split(' ')
    b = len(a)
    if b < 1:
        break
    else:
        if k == 1:
            for i in range(b-1):
                Mark_S.append(a[i])
        if k == 2:                    #Считывание характеристик машинок в другой файл
            for i in range(b-1):
                Body_Cars_S.append(a[i])
        if k == 3:
            for i in range(b-1):
                Engine_S.append(a[i])
        if k == 4:
            for i in range(b-1):
                Transmission_S.append(a[i])
        if k == 5:
            for i in range(b-1):
                Color_S.append(a[i])
        if k == 6:
            Doors_S.append(a[0])
            Doors_S.append(a[1])
        if k == 7:
            Headlights_S.append(a[0])
            Headlights_S.append(a[1])
        k += 1

f = open('Cars.txt','r+',encoding='utf-8')
while True:
    a = f.readline()
    a = a.split(' ')
    b = len(a)
    if b < 2:
        break
    else:                        #Считывание из файла данных и записывание их в соответствующие списки
        Marks.append(a[0])
        Body_Cars.append(a[1])
        Engines.append(a[2])
        Transmissions.append(a[3])
        Colors.append(a[4])
        Door_1_L.append(a[5])
        Door_1_R.append(a[6])
        Door_2_L.append(a[7])
        Door_2_R.append(a[8])
        Headlights.append(a[9])
        s+=1
f.close()

Car1 = Car(Marks, Body_Cars, Engines, Colors, Door_1_L, Door_1_R, Door_2_L, Door_2_R, Headlights, Mark_S, Engine_S, Body_Cars_S, Color_S, Transmissions, Transmission_S)


s3 = []
for i in range(s):
    s3.append(0)

while True:
    while True:
        print('1) Создать машинку')
        print('2) Редактирование параметров машинки')
        print('3) Просмотр машинок')
        print('4) Удаление машинок')
        print('5) Изменить колличество параметров')
        print('6) Выйти из программы')
        c = int(input('Выберите действие: '))
        if c < 1 or c > 6:
            print('Не корректный ввод')
        else:
            break

    if c == 1:
        Car1.Check_Mark()
        while True:
            a = int(input('Введите марку: '))
            if a >= 1 and a <= len(Mark_S):
                break
            else:
                print('Данные не корректны')
        Car1.Create_Mark(a)
        Car1.Check_Body_Car()
        while True:
            a = int(input('Введите кузов: '))
            if a >= 1 and a <= len(Body_Cars_S):
                break
            else:
                print('Данные не корректны')
        Car1.Create_Body_Car(a)
        Car1.Check_Engine()
        while True:
            a = int(input('Введите двигатель: '))
            if a >= 1 and a <= len(Engine_S):
                break
            else:
                print('Данные не корректны')
        Car1.Create_Engine(a)
        Car1.Check_Transmission()
        while True:
            a = int(input('Выберите коробку передач: '))
            if a >= 1 and a <= len(Transmission_S):
                break
            else:
                print('Данные не корректны')
        Car1.Create_Transmission(a)
        Car1.Check_Color()
        while True:
            a = int(input('Введите цвет: '))
            if a >= 1 and a <= len(Color_S):
                break
            else:
                print('Данные не корректны')
        Car1.Create_Color(a)
        Car1.Create_Door_1_L(Doors_S)
        Car1.Create_Door_1_R(Doors_S)
        Car1.Create_Door_2_L(Doors_S)
        Car1.Create_Door_2_R(Doors_S)
        Car1.Create_Headlights(Headlights_S)
        s = s +1
        s1 +=1
        s3.append(0)

    if c == 2:
        Car1.display_info()
        print('\n')
        while True:
            a = int(input('Выберите машинку, которую хотите редактировать: '))
            if a >= 1 and a <= s:
                break
            else:
                print('Данные не корректны')
        print('1) Изменить марку')
        print('2) Изменить кузов')
        print('3) Изменить двигатель')
        print('4) Изменить коробку передач')
        print('5) Изменить цвет')
        print('6) Изменить положение дверей')
        print('7) Изменить светимость фар')
        while True:
            m = int(input('Выберите параметр, который хотите изменить: '))
            if m >= 1 and m <= 6:
                break
            else:
                print('Данные не корректны')
        if m == 1:
            Car1.Check_Mark()
            Car1.Change_Mark(a,b)
        if m == 2:
            Car1.Check_Body_Car()
            Car1.Change_Body_Car(a,b)
        if m == 3:
            Car1.Check_Engine()
            Car1.Change_Engine(a,b)
        if m == 4:
            Car1.Check_Transmission()
            Car1.Change_Transmission(a,b)
        if m == 5:
            Car1.Check_Color()
            Car1.Change_Color(a,b)
        if m == 6:
            Car1.Change_Doors(Doors_S)
        if m == 7:
            Car1.Change_Headlights(Headlights_S)
            s3[a-1] = 1



    if c == 3:
        Car1.display_info()
        print('\n')

    if c == 4:
        Car1.display_info()
        print('\n')
        if s == 0:
            print('Нет машинок для удаления')
        else:
            a = int(input('Выберите машину, которую хотите удалить: '))
            Car1.Delete(a)
            s3.pop(a-1)
            if s > 0:
                s = s - 1

    if c == 5:
        Car1.Change_Characters()
        k = 1
        h = open('Specifications.txt', 'w+', encoding='utf-8')
        while k != 8:
            if k == 1:
                for i in range(len(Mark_S)):
                    h.write(Mark_S[i])
                    h.write(' ')
                h.write('\n')
            if k == 2:
                for i in range(len(Body_Cars_S)):
                    h.write(Body_Cars_S[i])
                    h.write(' ')
                h.write('\n')
            if k == 3:  ##Перезаписывание характеристик
                for i in range(len(Engine_S)):
                    h.write(Engine_S[i])
                    h.write(' ')
                h.write('\n')
            if k == 4:
                for i in range(len(Transmission_S)):
                    h.write(Transmission_S[i])
                    h.write(' ')
                h.write('\n')
            if k == 5:
                for i in range(len(Color_S)):
                    h.write(Color_S[i])
                    h.write(' ')
                h.write('\n')
            if k == 6:
                h.write('Открыта')
                h.write(' ')
                h.write('Закрыта')
                h.write(' ')
                h.write('\n')
            if k == 7:
                h.write('Вкл')
                h.write(' ')
                h.write('Выкл')
                h.write(' ')
            k += 1

    if c == 6:
        s2 = s1
        f = open('Cars.txt', 'w+', encoding='utf-8')
        if s == 1:
            f.write(Marks[0])
            f.write(' ')
            f.write(Body_Cars[0])
            f.write(' ')
            f.write(Engines[0])
            f.write(' ')
            f.write(Transmissions[0])
            f.write(' ')
            f.write(Colors[0])
            f.write(' ')
            f.write(Door_1_L[0])  # Считывание из файла данных и записывание их в соответствующие списки (если 1 машинка)
            f.write(' ')
            f.write(Door_1_R[0])
            f.write(' ')
            f.write(Door_2_L[0])
            f.write(' ')
            f.write(Door_2_R[0])
            f.write(' ')
            f.write(Headlights[0])
            f.close()
        else:
            for q in range(s):
                if (s2!=0 and s>1 and q+1>s-s1) and not(s>1 and s3[q]==1 and q != 0):
                    f.write('\n')
                    s2=s2-1
                    f.write(Marks[q])
                    f.write(' ')
                    f.write(Body_Cars[q])
                    f.write(' ')
                    f.write(Engines[q])
                    f.write(' ')
                    f.write(Transmissions[q])
                    f.write(' ')
                    f.write(Colors[q])
                    f.write(' ')
                    f.write(Door_1_L[q])  # Считывание из файла данных и записывание их в соответствующие списки
                    f.write(' ')
                    f.write(Door_1_R[q])
                    f.write(' ')
                    f.write(Door_2_L[q])
                    f.write(' ')
                    f.write(Door_2_R[q])
                    f.write(' ')
                    f.write(Headlights[q])
                elif not(s2!=0 and s>1 and q+1>s-s1) and (s>1 and s3[q]==1 and q != 0):
                    f.write(Marks[q])
                    f.write(' ')
                    f.write(Body_Cars[q])
                    f.write(' ')
                    f.write(Engines[q])
                    f.write(' ')
                    f.write(Transmissions[q])
                    f.write(' ')
                    f.write(Colors[q])
                    f.write(' ')
                    f.write(Door_1_L[q])  # Считывание из файла данных и записывание их в соответствующие списки
                    f.write(' ')
                    f.write(Door_1_R[q])
                    f.write(' ')
                    f.write(Door_2_L[q])
                    f.write(' ')
                    f.write(Door_2_R[q])
                    f.write(' ')
                    f.write(Headlights[q])
                    f.write('\n')
                elif (s2!=0 and s>1 and q+1>s-s1) and (s>1 and s3[q]==1 and q != 0):
                    f.write('\n')
                    s2 = s2 - 1
                    f.write(Marks[q])
                    f.write(' ')
                    f.write(Body_Cars[q])
                    f.write(' ')
                    f.write(Engines[q])
                    f.write(' ')
                    f.write(Transmissions[q])
                    f.write(' ')
                    f.write(Colors[q])
                    f.write(' ')
                    f.write(Door_1_L[q])  # Считывание из файла данных и записывание их в соответствующие списки
                    f.write(' ')
                    f.write(Door_1_R[q])
                    f.write(' ')
                    f.write(Door_2_L[q])
                    f.write(' ')
                    f.write(Door_2_R[q])
                    f.write(' ')
                    f.write(Headlights[q])
                else:
                    f.write(Marks[q])
                    f.write(' ')
                    f.write(Body_Cars[q])
                    f.write(' ')
                    f.write(Engines[q])
                    f.write(' ')
                    f.write(Transmissions[q])
                    f.write(' ')
                    f.write(Colors[q])
                    f.write(' ')
                    f.write(Door_1_L[q])  # Считывание из файла данных и записывание их в соответствующие списки
                    f.write(' ')
                    f.write(Door_1_R[q])
                    f.write(' ')
                    f.write(Door_2_L[q])
                    f.write(' ')
                    f.write(Door_2_R[q])
                    f.write(' ')
                    f.write(Headlights[q])
            f.close()
        break


