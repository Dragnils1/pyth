list = ['asd', 'asdsa', ';sd', 'sdadasds']

#start (include), end, step
print(list[0:2:1]) # ['asd', 'asdsa']
print(list[-1:]) # show oly last elem ['sdadasds']
print(list[:2]) # to second and not include ['asd', 'asdsa']
print(list[::-1]) # reverse list ind go from end to start (['sdadasds', ';sd', 'asdsa', 'asd'])

list[1::1] = ['only', 'common', 'attempting','do', 'best','the']
print(list) # ['asd', 'only', 'common', 'attempting', 'do', 'best', 'the']