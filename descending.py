num_array = raw_input("Enter a num:")
b = map(int,num_array)
n=[]
while b:
    smallest = min(b)
    n.append(smallest)
    b.remove(smallest)
print
print ''.join(map(str, n))
'''
for j in range(len(num_array)):

    for i in range(len(num_array)-1):

        if num_array[i]<num_array[i+1]:

            temp = num_array[i]
            num_array[i]=num_array[i+1]
            num_array[i+1] = temp

print("Sorted Array is:",num_array)
'''
