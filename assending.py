import random

from random import randint

num_array = []

while len(num_array) <10:

    num_array.append(random.randint(1,100))

print("Unsorted array is:",num_array)

for j in range(len(num_array)):

    for i in range(len(num_array)-1):

        if num_array[i]<num_array[i+1]:

            temp = num_array[i+1]
            num_array[i+1]=num_array[i]
            num_array[i] = temp

print("Sorted Array is:",num_array)
