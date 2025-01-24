"""
Griffin Stover
1-24-25
23199
CIS 226
Time Estimate: 30 minutes
"""
#Design: I will solve the problem by implementing code that searches line by line to find the given text.
#Develop: I used a for loop to iterate through each line, and print out the line that contains the desired text.
#Test: I tested for cases where there are not enough arguments, and cases where the given file is not found.
#Document: This code is meant to be used as a clone of grep. 
#User Documentation: This program can be used at the command line as follows: python main.py (desired search term) (filename). From there it will display the line that contains the word you are 
#searching for. It will also display an error message if the desired term is not found, if you are missing arguments, or if the file could not be found.
import sys

def do_grep(search_text, filename):
    f = open(filename)
    found = 0
    for line in f: 
        if search_text in line:
            print(line)
            found += 1
    if found == 0:
        print("Not found in file.")

    

def main():
    # TODO: Check len(sys.argv) and warn if missing arguments
    try:
        search_text = sys.argv[1]
        filename = sys.argv[2]
    except Exception:
        print("Missing arguments")
        return 0

    try:
        do_grep(search_text, filename)
    except FileNotFoundError:
        print("File could not be found.")
    

if __name__ == '__main__':
    main()



