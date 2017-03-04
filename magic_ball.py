import random
def getAnswer(answerNumber):
    if answerNumber==1:
        return 'No its not'
    if answerNumber==2:
        return 'You are just missed'
    if answerNumber==3:
        return 'Shakuni mama'
    if answerNumber==4:
        return 'Sab mohmaya hai'
    if answerNumber==5:
        return 'kasa vatatay'
    if answerNumber==6:
        return 'hahahahahah'
    if answerNumber==7:
        return 'kjfdfahsk'
    if answerNumber==8:
        return 'You''re ne to answer'
    if answerNumber==9:
        return 'Finally you did it'
r=random.randint(1,9)
fortune=getAnswer(r)
print(fortune)

