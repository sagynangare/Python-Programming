sp = 1200
cp = 1200
if (sp>cp):
    print "Congrats"
    print "You've made a profit of", sp-cp,"bucks"
elif (cp>sp):
    print("Oops!")
    print("You've made a loss of", cp-sp,"bucks")
else:
    print "you didn't have profit or loss"
