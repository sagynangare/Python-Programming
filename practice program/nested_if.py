char = raw_input("Enter keyward")
if ord(char)>=65 and ord(char)<=90:
    print "You entered an upper case alphabet"
    if char in ('A','E','I','O','U'):
        print "You entered a vovel."
    else:
        print "You entered a consonant."
elif ord(char)>=97 and ord(char)<=122:
    print "You entered an upper case alphabet"
    if char in ('a','e','i','o','u'):
        print "You entered a vovel."
    else:
        print "You entered a consonant."
else:
    print "You are not entered anything.... Please try again"
