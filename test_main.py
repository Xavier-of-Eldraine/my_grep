# test_main.py
from main import do_grep

def test_do_grep():
    do_grep("chicken","animals.txt")
    do_grep("Horse")
    do_grep("dog","animal.txt")
    

test_do_grep()