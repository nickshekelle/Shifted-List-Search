# Shifted-List-Search

This is a Python fuction to return the maximum element in a "shifted list"
An example of a shifted list is as follow:
```
initial_list = [1, 3, 7, 8, 9, 10, 11]  # Here is our initial ordered list
shifted_list = [8, 9, 10, 11, 1, 3, 7]  # Here is the list after it has been sliced (at index 3) and shifted
```
I decided to go with a modified binary search solution. I initially came up with a brute force solution which ran in O(n)
```
# Brute Force:
def findLargest(x):
	max = 0
	for i in x:
		if i>max:
			max = i
	return max
 ```
 This solution does not exploit the given information that the list is sorted in two pieces. I modified binary search to account for these
 two seperate sorted pieces and came up with the optimal solution, O(logn) with O(1) space. 
 
 There is one problem with my solution however. In the case of a list that does not have distinct elements, meaning that there are repeated 
 elements in the list, my binary search may fail to return the maximum value. In the case of nondistinct lists, the best possible runtime 
 for finding the maximum seems to be O(n). I have implemented a way to catch if there are nondistinct values, and if there are, I run the 
 brute force solution.
 

- Can you identify any edge cases that we need to account for?

I accounted for the edge case of an empty list in my code. My function should have no problem running efficiently on massive lists.

- Can you explain the orders of growth implications of the algorithm you implemented?

My function uses binary search. For all distinct inputs of length n, it will return the largest element with O(logn) time complexity.
For non-distinct inputs of length n, it will return the largest element with O(n) time complexity.

- Suppose our initial list contains 1 million elements, is there a more performant way we can find the answer?

My function is as optimal as you can get for the specified problem. It will run very quickly if all the elements in the list are distinct and not nearly as quick if they are not distinct. 
