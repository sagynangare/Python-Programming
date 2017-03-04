### Print the numbers 1..100. for multiple of 3, print "Fizz" instead of the number.
###for multiple of 5, print "Buzz" instead of the number.for multiples of 3 and 5, print "Fizzbuzz" instead of the number.
##
##counter =0
##while counter < 101:
##    if counter % 3==0 and counter % 5 == 0:
##        print (counter," is FizzBuzz")
##    elif counter % 3 == 0:
##        print( counter," is Fizz.")
##    elif counter % 5 ==0:
##        print( counter," is Buzz.")
##    else:
##        print(counter, " is number.")
##    counter = counter + 1
##    print counter
##        


def fib(num):
    a,b =0,1
    for i in range(0,num):
        yield "{}: {}".format(i+1, a)
        a,b = b,a + b
for item in fib(10):
    print item
