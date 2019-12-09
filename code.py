def key(slovar, number):
    a = []
    for i in slovar:
        a.append(i)
    return a[number-1]
Capitals = {'Russia': 'Moscow', 'Ukraine': 'Kiev', 'USA': 'Washington'}
print(key(Capitals ,2))