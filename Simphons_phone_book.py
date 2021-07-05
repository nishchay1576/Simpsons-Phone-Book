# -*- coding: utf-8 -*-
#Simpsons Phone Book

"""
    There are some people with the surname 'Neu'. 
    We are looking for a 'Neu', but we don't know the 
    first name, we just know that it starts with a 'J'. 
    Let's write a Python script, which finds all the lines of 
    the phone book, which contain a person with the described 
    surname and a first name starting with 'J'. 
 Hint: 
     Use Regular Expressions 
 
 Output:
     Jack Neu 555-7666
     Jeb Neu 555-5543
     Jennifer Neu 555-3652
"""

import re
file = open('/Users/nishchay/Documents/datafiles/simpsons_phone_book.txt','r')

for text in file:
    if (re.search(r'^J\w*\s*Neu',text)):
        print(text)

file.close()