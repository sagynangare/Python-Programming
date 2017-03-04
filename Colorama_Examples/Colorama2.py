from colorama import *

def pos(x, y):
    return '\x1b['+ str(y) + ';' + str(x) + 'H'
def main():
    
    init()
    
    print(Fore.RED + pos(30,10) + "Sagar is" )

    raw_input()

if(__name__=="__main__"):
    main()
