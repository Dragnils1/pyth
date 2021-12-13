#!/usr/bin/env python
import nltk

# Echo the contents of a file
# f = open('foo.txt', 'rU')
# for line in f:   ## iterates over the lines of the file
#     print (line)   ## trailing , so print does not add an end-of-line char
#                 ## since 'line' already includes the end-of-line.
# f.close()



with open("book.txt") as infile:
    count = len(nltk.word_tokenize(infile.read()))
    print(count)