# Shifted List Search

# Brute force solution:
# def findLargest(x: List[int]):
#	max = 0
#	for i in x:
#		if i>max:
#			max = i
#	return max
#
# Problem with brute force: runtime is O(n)


def findLargest(x, low, high):

	# Edge case: empty list
	if not x:
		print("List is Empty")
		return -1

	lo = low
	hi = high
	mid = (hi + lo)//2
	
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
 

