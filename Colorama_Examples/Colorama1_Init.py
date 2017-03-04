from colorama import *

def main():
    init()
    
    print(Style.NORMAL)
    print(Back.WHITE + Fore.MAGENTA + "Sagar is" + Fore.RED +" Loves")
    print(Style.RESET_ALL)
    raw_input( )

if(__name__=="__main__"):
    main()
