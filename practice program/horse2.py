def computepay(h,r):
    if h<=40:
        p=h*r
    else:
        p=r*40+(r*1.5*(h-40))
        print("Finished with computepay",p)
        return p
            
try:
    inp=input("Enter hourse: ")
    hourse=float(inp)
    inp=input("Enter Rate: ")
    rate=float(inp)
except:
    print("Error,Please enter numeric input")
    quit()
print("In the main code",rate,hourse)
pay= computepay (rate,hourse)

print("We are back",pay)
