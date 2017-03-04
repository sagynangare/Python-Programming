def merge(list1, list2):
    output = []
    i = 0
    j = 0
    length1 = len(list1)
    length2 = len(list2)

    while i < length1 or j < length2:
        if i<length1 and j < length2:
            if list1[i] <= list2[j]:
                output += [list1[i]]
                i = i+1
            else:
                output +=[list2[j]]
                j = j + 1
        elif i<length1:
            output += [list1[i]]
            i = i + 1
        else:
            output += [list2[j]]
            j = j+1
        return output
print (merge([1,2],[-1,3,5]))
