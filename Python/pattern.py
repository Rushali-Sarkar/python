#!/usr/bin/python3

import platform

def main():
        message()

def message():
        print("This is python version {}".format(platform.python_version()))
        print("Line 2")
        print("Line 3")
        print("Line 4")
        if False: # This is a comment
                print("Line 5") # this is another comment
        else:
                print("not true")

if __name__ == "__main__":
        main()
