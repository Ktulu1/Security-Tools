# url unescaper
# command line argument is filename

import urllib.parse
import os
from sys import argv

script, filename = argv
text = []
linenum = 0

def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')



with open (filename, 'rt') as file:                         # open file for read and text 'rt', keep it open, close it when done
    for line in file:                                       # loop "line" in "searchfile"
        linenum += 1                                        # increment linenumber
        text.append(urllib.parse.unquote(line))

clear_screen()

for results in text:                                        # loop "results" into list "text"
    print(str(results))                                     # print "results"



