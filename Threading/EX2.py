import threading


def do_this():
    print("Hello, This is our thread!")
    global dead

    x= 0
    
    while( not dead ):
        x +=1
        pass
    print x

    
def main():

    global dead
    dead = False

    our_thread = threading.Thread( target = do_this )
    our_thread.start()

    
    print (threading.active_count())
    print (threading.enumerate())
    print(threading.current_thread())

    raw_input("Hit ENTER to die")
    dead = True


if(__name__ == "__main__"):
    main()
