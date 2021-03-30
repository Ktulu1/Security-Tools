# text file search
# plain text and regex
# command line arguments are filename and search string 

import re
import os
from sys import argv

script, filename, searchstr = argv
text = []
linenum = 0                                              
pattern = re.compile(searchstr, re.IGNORECASE)              # create a pattern object called "pattern" from "searchstr" and ignore case

def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

with open (filename, 'rt') as searchfile:                   # open searchfile, keep it open, close it when done
    for line in searchfile:                                 # loop "line" in "searchfile"
        linenum += 1                                        # increment linenumber
        if pattern.search(line) != None:                    # search line for "pattern" if not equal to none do next
            text.append((linenum, line.rstrip('\n')))       # append list "text" with line numbers and line text with striped linefeeds

clear_screen()

for results in text:                                        # loop "results" in list "text"
    print("Line", str(results[0]), ": " + results[1])       # print "results" with line numbers


