message='It was a bright cold day in April and the clocks were stricking thirteen'
count={}
for charactor in message.Upper:
    count.setdefault(charactor,0)
    count[charactor]=count[charactor]+1
    print(count)
    
print("Thank you for your time :-)")
