with open('devices.csv', 'r', encoding='utf-8') as file:
    reader = file.read().split('\n')
    a = input()
    while a != '666':
        t = True
        for b in reader[1::]:
            y = b.split(';')
            if y[1] == a:
                if t:
                    print(f'По вашему запросу: {a} найдены следующие варианты:')
                    t = False
                print(f'{y[0]} {y[1]} - тип устройства: {y[2]}; Разрешение экрана - {y[3]}; Цена - {y[-1]}')
        if t:
            print('У нас нет данного устройства')
            break
        a = input()