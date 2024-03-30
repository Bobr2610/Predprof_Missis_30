data = []
with open('devices.csv', 'r', encoding='utf-8') as file:
    reader = file.read().split('\n')
    for a in reader[1::]:
        y = a.split(';')
        data.append(y)

der = data
for i in range(len(der)):
    for j in range(len(der)):
        if der[i][0] < der[j][0]:
            s = der[i][0]
            der[i][0] = der[j][0]
            der[j][0] = s
k = 0
for w in der[::-1]:
    print(f'{w[0]} - {w[1]} - {w[-1]}')
    k += 1
    if k == 5:
        break