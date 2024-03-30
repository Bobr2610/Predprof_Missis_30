data = {}
with open('devices.csv', 'r', encoding='utf-8') as file:
    reader = file.read().split('\n')
    for a in reader[1::]:
        y = a.split(';')
        if y[0] in data.keys():
            data[y[0]] += 1
        else:
            data[y[0]] = 1

with open('count_company.csv', 'w', encoding='utf-8') as new_file:
    new_file.writelines('Company,countProduct\n')
    for i in data.keys():
        new_file.writelines(f'{i},{data[i]}\n')