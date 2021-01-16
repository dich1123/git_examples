# DICTIONARY

# словарь - это изменяемый ТД.
example = {}  # это пустой словарь
print(type(example))
print(example)

data = {'key1': 'value1', 'key2': 'value2'}

# ключем может выступать только хэшируемый ТД. то что является неизменяемым ТД.
# значением может выступать любой ТД

data = {'key1': 'value1', 'key2': data}
data = {'key1': 'value1', 'key2': data}
print(data)

# получение значения по ключу - быстрая операция(O(1))
# получение ключей по значению - медленная операция(O(n))

# ключи - это уникальные значения для одного словаря

data = {'1': ['lol', '2']}

print(data['1'])  # чтоб получить значение по ключу нужно обратиться к словарю в скобках указав ключ
data['2'] = 'new value'  # чтоб создать новую пару обращаемся по несуществующему ключу и передаем новое знач
print(data)

data['1'] = 'lolkek'  # чтоб перезаписать значение по ключу: обращ по сущ ключу и передаем новое знач
print(data)

lol = data.pop('1')  # pop удаляет пару по ключу и возвращает значение
print(lol)
print(data)

data.update({'3': '3_data', 4: '4_data'})  # расширит словарь парами из словаря-аргумента
print(data)
data2 = {'2': 'lolkek'}
data2['3'] = {'3': '3_data',
              4: '4_data'}
print(data2)

print(len(data2))  # длинна - это кло-во пар в словаре

# варианты прохода по словарю
# 1
for i in data.keys():  # пройтись по всем ключам словаря
    print(i)

# 2
for i in data.values():  # пройтись по всем значениям в словаре
    print(i)

# 3
for key, value in data.items():  # пройтись по парам ключ-значение
    print(key, value)

# ADD EXTRA DATA FROM OTHER DEV


print('USEFUL DATA CODE PRINTING VERY IMPORTANT NOT DELETE YOU WiLL DIE CORONA WINS')
print('USEFUL DATA CODE PRINTING VERY IMPORTANT NOT DELETE YOU WiLL DIE CORONA WINS')
print('Some useful code from feature_branch1')
