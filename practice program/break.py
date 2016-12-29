while True:
    print("Enter a digit:")
    num = raw_input()
    var = str(num)
    if(ord(var) in range(48,58)):
        break
print ("You are very obedient!")
