#3.1
import sys
import os

def wc(file):
    """
    Inputs filename in same directory as wc.py.
    Returns tuple with number of
    lines, words, characters, and filename of the input file.
    """

    infile = open(str(file), "r")

    words = []
    lines = 0
    for line in infile:
        lines += 1
        words += line.split()

    char = 0
    for word in words:
        for character in word:
            char += 1

    return lines, len(words), char, str(file)

def execute():
    """
    Read command line args. and execute front-end of program.
    """

    #word count all compatible files in directory
    if str(sys.argv[1]) == "*":
        for file in os.listdir():
            try:
                print(wc(file))

            except:
                print("WARNING: Could not read %s properly" % file)

    #word count all python files in directory
    elif str(sys.argv[1]) == "*.py":
        for file in os.listdir():
            if str(file)[-3:] == ".py":
                print(wc(str(file)))

    #word count input file in directory
    else:
        file = str(sys.argv[1])
        print(wc(file))

if __name__ == '__main__':
    execute()
