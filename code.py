math = {'qst1': ['ask', 'ask1', 'ask2', 'ask3'],
        'qst2': ['asks', 'asks1', 'asks2', 'asks3']}

idk = {'qst1': ['ask', 'ask1', 'ask2', 'ask3'],
       'qst2': ['asks', 'asks1', 'asks2', 'asks3']}


def key(slovar, number):
    keys = []
    if number <= len(slovar):
        for i in slovar:
            keys.append(i)
    return keys[number - 1]
