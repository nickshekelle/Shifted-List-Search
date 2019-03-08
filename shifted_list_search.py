# Shifted List Search

# This import is only used for testing
#import random 


# returns the largest element in a shifted list
def findLargest(x, low, high):

    # Edge case: empty list
    if not x:
        print("List is Empty")
        return -1

    lo = low
    hi = high
    mid = (hi + lo)//2

    # if there are duplicate elements
    if x[lo] == x[lo+1] or x[hi] == x[hi-1] or x[lo] == x[hi] or x[mid] == x[mid-1] or x[mid] == x[mid+1]:
        return findLargest_iterative(x)
    
    # if x[lo] < x[hi], then the array was not rotated
    if x[lo] < x[hi]:
        return x[hi]

    # if there is only one element
    if hi == lo:
        return x[lo]

    # if x[mid] > x[hi], we know the biggest element is between mid and hi
    if x[mid] > x[hi]:
        # if x[mid+1] > x[mid], we can eliminate x[mid] from possible largest values
        if x[mid+1] > x[mid]:
            return findLargest(x, mid+1, hi)
        else:
            # if x[mid+1] < x[mid], then x[mid + 1] is the point of rotation, so x[mid]
            # is the largest element in our array
            return x[mid]
    else:
        # if x[hi] > x[mid], we know the largest element is between lo and mid
        return findLargest(x, lo, mid)
 

def findLargest_iterative(x):
    print("Iterative!")
    max = 0
    for i in x:
        if i>max:
            max = i
    return max



# Test for findLargest
#for l in range(0, 10000):
#  x = []
#  for i in range(0,1000):
#    x.append(random.randint(-1000000,1000000))
#  x.sort()

#  if len(x) != len(set(x)):
#    print("There are duplicates")

#  k = x[len(x)-1]
#  y = random.randint(1, len(x)-1)
#  z = x[:y]
#  j = x[y:]
#  j = j + z

#  if k == findLargest(j, 0, len(j)-1):
#    if iterative == True:
#      print("Used iterative method")
#    print("Sucess!")
#  else:
#    print("FAILED")
#    break
