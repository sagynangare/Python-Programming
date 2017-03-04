from unicurses import *

def main():
    stdscr = initscr()

   
    addstr("Hellow World")
    
    endwin()
    return 0

if (__name__ == "__main__"):
    main()
