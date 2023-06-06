# url unescaper for URL encoding
# command line argument is filename

import urllib.parse
import os
from sys import argv

script, filename = argv
text = []
linenum = 0

def clear_screen():                                         # function to clear screen 
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')



with open (filename, 'rt') as file:                         # open file for read and text 'rt', keep it open, close it when done
    for line in file:                                       # loop "line" in "searchfile"
        linenum += 1                                        # increment linenumber
        text.append(urllib.parse.unquote(line))             # append list "text" with lines parsed lines from file

clear_screen()

for results in text:                                        # loop list "text" into "results"
    print(str(results))                                     # print "results"



