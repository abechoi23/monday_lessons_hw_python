"""
Given an list nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Example Input: [0,0,11,2,3,4]
Example Output: [11,2,3,4,0,0]
"""

# input list numbers
# output list

# look at every number
# decide if number is zero or not
# if zero remove from current position 
# if not a zero 

# loop
# conditional compare to zero
# if zero .pop()
# .append zero

def move_zeros(alist):
    output = []
    i=0
    while i < len(alist) - alist.count(0):
        print(i, alist[i])
        if alist[i] == 0:
            alist.pop(i)
            alist.append(0)
            print(alist)
        else:
            i+=1
    return alist

print(move_zeros([0,0,11,2,3,4]))