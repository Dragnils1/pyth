from sys import getdefaultencoding


# Python 3 ====================

getdefaultencoding()  # utf-8

my_bytes = 'котобус cat'.encode()

my_bytes.decode('ascii', errors='backslashreplace')
# '\\xd0\\xba\\xd0\\xbe\\xd1\\x82\\xd0\\xbe\\xd0\\xb1\\xd1\\x83\\xd1\\x81 cat'

my_bytes.decode('ascii', errors='surrogateescape')
# '\udcd0\udcba\udcd0\udcbe\udcd1\udc82\udcd0\udcbe\udcd0\udcb1\udcd1\udc83\udcd1\udc81 cat'





# Возвращает символ (в виде строки), чья позиция кода для Юникод равна указанному целому i. 
# Аргумент должен располагаться в пределах от 0 до 1,114,111 (0x10FFFF), 
# в противном случае возбуждается исключение

# Возвращает символ по его числовому представлению.
# chr(i) -> str





# Возвращает числовое представление для указанного символа.
# ord(chr) -> int
