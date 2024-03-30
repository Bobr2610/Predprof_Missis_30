data = []
with open('devices.csv', 'r', encoding='utf-8') as file:
    reader = file.read().split('\n')
    alp1 = sorted('цукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ')
    d = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    B = alp1[:32]
    b = alp1[32:]
    q = ''
    for i in b:
        q += str(i) + ' ,'
    for i in B:
        q += str(i) + ' ,'
    dA = sorted(d)[:26]
    da = sorted(d)[26:]
    for i in da:
        q += str(i) + ' ,'
    for i in dA:
        q += str(i) + ' ,'
    for a in reader[1::]:
        y = a.split(';')
        s = y[0]+' '+y[1]
        m_1 = True
        m_2 = True
        m_3 = True
        for n in range(len(s)):
            if s[n] not in da:
                m_1 = False
            if s[n] not in dA and s[n] not in da:
                m_2 = False
            if s[n] not in alp1:
                m_3 = False
        e = ('  ,' + q).split(' ,')
        if m_1:
            p = 31
        elif m_2:
            p = 53
        elif m_3:
            p = 67
        m = 10**9 + 9
        v = 0
        for n in range(len(s)):
            v += e.index[s[n]] * (p ** (len(s) - n))
        data.append(y+[v])
print(data)