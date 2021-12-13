
from sys import getdefaultencoding

# Python 3 ====================

getdefaultencoding()  # utf-8

my_string = 'кот cat'

type(my_string)  # str

my_string.encode()
# b'\xd0\xba\xd0\xbe\xd1\x82 cat'

my_string.encode('ascii')
# UnicodeDecodeError

my_string.encode('ascii', errors='ignore')
# b' cat'

my_string.encode('ascii', errors='replace')  
# b'??? cat'

my_string.encode('ascii', errors='xmlcharrefreplace')
# b'кот cat'

my_string.encode('ascii', errors='backslashreplace')
# b'\\u043a\\u043e\\u0442 cat'

my_string.encode('ascii', errors='namereplace')
# b'\\N{CYRILLIC SMALL LETTER KA}\\N{CYRILLIC SMALL LETTER O}\\N{CYRILLIC SMALL LETTER TE} cat'

surrogated = '\udcd0\udcba\udcd0\udcbe\udcd1\udc82 cat'

surrogated.encode()  
# UnicodeEncodeError

surrogated.encode(errors='surrogateescape')
# b'\xd0\xba\xd0\xbe\xd1\x82 cat'

surrogated.encode(errors='surrogatepass')
# b'\xed\xb3\x90\xed\xb2\xba\xed\xb3\x90\xed\xb2\xbe\xed\xb3\x91\xed\xb2\x82 cat'