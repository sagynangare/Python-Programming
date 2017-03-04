import hashlib, getpass
from colorama import *


def main():
    init()
    filename = "save_data"
    save_data = open(filename, 'U+')
    contents = save_data.read()

    code = hashlib.sha512()
    
    print (Fore.GREEN + "Hello, Welcome to the Sagar's blog")
    print (Fore.RESET + "Please login by entering passward" )
    if (contents == ''):
        print(Fore.YELLOW + Style.BRIGHT + "You Need to create a pass\
              word to be login shell")
        passward = getpass.getpass( )
        code.update(passward)
        save_data.write(code.hexdigest())
        print(Fore.GREEN + "\n\ Success\n\n \
                we stored your passward")
        else:
            print(Fore.RED + Style.BRIGHT + "\n You need to  create \
                a passward to be able to log in with")
            

    print(Fore.GREEN + "=========== \n\n" + Fore.YELLOW + Style.BRIGHT)
    
    print(Fore.RESET + Style.RESET_ALL)
    code = hashlib.sha512(passward).hexdigest()
    print(code)


if (__name__=="__main__"):
    main()
