a,b = 0,1
for num in xrange (0,10):
    print a
    a,b = b,a+b

#Give me each number in a list squared
my_list = [1,2,3,4,5,6,7,8,9,10]
squared = [num*num for num in my_list]
print squared
