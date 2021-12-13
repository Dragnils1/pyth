#[[fill]align][sign][⌗][0][width][.precision][typecode]

'|{:<20}| - выравниваем по левому краю'.format('XX') # '|XX                  | - выравниваем по левому краю'
'|{:>20}| - выравниваем по правому краю'.format('XX') # '|                  XX| - выравниваем по правому краю'
'|{:_^20}| - выравниваем по центру с заполнителем'.format('XX') # '|_________XX_________| - выравниваем по центру с заполнителем'


d = {'name':'Andrey', 'age':21}

# Вместо:

# print('My name is ' + d['name'] + '. I am' + str(d['age']) +'years old')

# Можно написать так:

print(f'My name is {d["name"]}. I am {d["age"]} years old.')