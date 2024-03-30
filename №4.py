data = {}
with open('devices.csv', 'r', encoding='utf-8') as file:
    reader = file.read().split('\n')
    for a in reader[1::]:
        y = a.split(';')
        if y[0] in data.keys():
            data[y[0]] += float(y[-1].replace(',', '.'))
        else:
            data[y[0]] = float(y[-1].replace(',', '.'))
print(data)

for i in data.keys():
    print(f'Если продать все ноутбуки {i} можно заработать {data[i]}.')