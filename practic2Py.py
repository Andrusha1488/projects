person = {}


def Hello():
    while True:
        name = input("Введите имя ")
        try:
            age = int(input("Введите возраст "))
            person = {
                "name": name,
                "age": age
            }
            break
        except:
            print("ошибка")

    person = person
    tempname = person["name"]
    print(f'Добро пожаловать, {tempname}')


Hello()

print('''Голова болела, а вы проснулись от жужащего под ухо будильника. Глаза устали, после долгой игровой сессии ночью, а теперь еще и придется идти в шарагу.''')

stop = []


def sujet():
    while (stop != [1, 2, 3, 4, 5]):
        GoOrNot()
        stop.append(1)

        BoringCollege()
        stop.append(2)

        Rest()
        stop.append(3)

        StayOrLeave()
        stop.append(4)

        SpendingFreetime()
        stop.append(5)


collections = []


def GoOrNot():
    print('Стоит ли в принципе идти куда то?')
    i = 0
    while (i != 2):
        print('1) Полежу чуть подольше...\n2) Нет, нужно идти в шарагу\n3) В доте еще не апнут первый страж, надо зайти в игру')
        try:
            i = int(input())
            if (i == 1):
                print("Еще немного полежу, так уж и быть, не хватает сна...\n и еще чуть чуть...\nи еще чутка...\nвскоре - вы задремали\nНет, нужно просыпаться!")
            elif (i == 2):
                print("Вот и правильно, пора уже взяться за ум и учить питон")
                print("Дорога до шараги была нетрудной, и вы налегке добрались")
            elif (i == 3):
                print(
                    "Дота это классно, но непора ли задуматься о чем то другом? не тошнит ли от игр?")
            else:
                print("Вы выбрали неправильное действие, выбирите из списка.")
        except ValueError:
            print("Введите цифру")


def BoringCollege():
    print("Вот вы и в шараге, скучно, что бы поделать?")
    while (True):
        print("1) Пойти в столовку\n2) Сходить на пары по питону\n3) Прогулять")
        try:
            i = int(input())
            if (i == 2):
                print(
                    "Вот это правильно, вот это хорошо, учить питон это правильно")
                print("Вы получили достижение 'Змеевод'")
                collections.append("Змеевод,")
                break
            elif (i == 1):
                print("Ужасно, на багеты с колбасой вам не хватает карманных денег")
            elif (i == 3):
                print("Ты куда пошел?' - кричат дежурные. Надо вернуться")
            else:
                print("Действия не существует.")
        except ValueError:
            print("Введите ту цифру")


def Rest():
    print(
        "Пара прошла отлично, вы уже не обязаны сидть и можете сходить куда то")
    i = 0
    while (True):
        print("1)Время по*урить\n2)Время сходить и уже наконец покушать (мама скинула денег)\n3)посижу здесь и подожду следующей пары")
        try:
            i = int(input())
            if (i == 1):
                print("Вы чего, мы не курим! и вам не советуем. Вы поднялись обратно к кабинету")
                print("Вы получили достижение 'Главный эколог'")
                collections.append("Главный эколог,")
                break
            if(i == 2):
                print('Наконец- то сходим в miratorg и покушаем пиццы\nкусочек другой, и вы уже наелись, можно идти обратно.')
                break
            elif (i == 3):
                print("Время быстро пролетает, вы не замерзли и сидите около кабинета")
                print("Вы получили достижение 'Мудрец'")
                collections.append("Мудрец,")
                break
            else:
                print("Действия не существует")
        except ValueError:
            print("Введите цифру")


def StayOrLeave():
    print(
        "Ну вот! Опять пара! А может...")
    i = 0

    while (True):
        print("1)Свалить домой\n2)Остаться\n")
        try:
            i = int(input())
            if (i == 1):
                print("На этот раз прокатит, в такое время никого в шараге нет! Вы свалили и успешно добрались до дома")
                print("Вы получили достижение 'Наглец'")
                collections.append("Наглец,")
                break
            if(i == 2):
                print('Вы же хороший ученик, посидите еще одну пару... Проходит время и скучная пара заканчивается. Теперь можно идти домой, хоть вы очень устали')
                print("Вы получили достижение 'Отличник'")
                collections.append("Отличник,")
                break
            else:
                print("Действия не существует")
        except ValueError:
            print("Введите цифру")


def SpendingFreetime():
    print(
        "Вот вы и дома, очень насыщенный день, не так-ли? можно отдохнуть")
    i = 0
    while (True):
        print("1)ОО дааа. Дота!\n2)Делать практическую по питончику...\n3)Наконец-то поспать")
        try:
            i = int(input())
            if (i == 1):
                print("ДААААА! Вы безудержно играете весь вечер и ныряете в кроватку")
                break
            if(i == 2):
                print('О нет! Вы вовремя вспоминаете о практической работе на завтра по питончику. у вас еще есть время ее сделать. После упорных стараний, все получается и вы утопаете во сне...')
                break
            elif(i == 3):
                print('Вы уляглись на кровати, но глаза не закрываются от навязчивых мыслей. Стоит попробовть что-то другое')
            else:
                print("Действия не существует")
        except ValueError:
            print("Введите цифру")


sujet()
print('''Спасибо за игру, дорогой пользователь! ''')
print("Ваши достижения:", *collections)