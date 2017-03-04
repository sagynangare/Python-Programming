'''def iq_test(nums):
    nums = '1 2 3 5 7'
    odd = []
    even = []
    for i,num in ((i,int(num))for (i,num) in enumerate(nums.split(' '))):
        odd.append((i,num) if num % 2!=0 else even.append(i,num))
        if len(odd)>1 and even:
            return even[0][0] +1
        elif len(even) > 1 and odd:
            return odd[0][0]+1
iq_test(3)
   '''
def iq_test(nums(str)):
    """One number is odd while other are even, or vise versa - find it
    Args:
        nums (str): '1 2 11 ...'
    Returns:
        int: Position of differ number + 1
    Examples:
        >>> iq_test('2 4 6 7 8')
        4
    """
    odd = []
    even = []
    for i, num in ((i, int(num)) for (i, num) in enumerate(nums.split(' '))):
        odd.append((i, num)) if num % 2 != 0 else even.append((i, num))
        if len(odd) > 1 and even:
            return even[0][0] + 1
        elif len(even) > 1 and odd:
            return odd[0][0] + 1
iq_test('2 4 6 7 8')
