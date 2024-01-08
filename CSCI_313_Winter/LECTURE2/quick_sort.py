'''
Implementing quick sort algorithim

- choose pivot element (usually last element in array)
- store elements left than pivot in left subarray and greater in right subarray
- call quicksort recursively on left and right until single elements
- combine the elements

we use i, j, and p i = begin, j = p - 1, p = end
i goes from left to right -> i looks for ele > p
j goes from right to left - > j look for ele < p
so then swap i and j
if i is not left than j they have crossed
if they have crossed swap i and p

'''

def quick_sort(arr, left, right):
  # left and right are indexes that determine the parts of the array we want to sort
  # if the length is 1 quicksort donsnt need to sort
  if left < right: # if its not true -> only 1 element or 0
    partition_position = partition(arr, left, right)
    quick_sort(arr, left, partition_position - 1) # call quicksort on all ele < pivot
    quick_sort(arr, partition_position + 1, right) # call quicksort on all ele > pivot
  return arr

def partition(arr, left, right):  # returns piv
  i = left 
  j = right
  pivot = arr[right]

  while i < j: # while they havent crossed
    while i < right and arr[i] < pivot: # while i has not reached the pivot
      i += 1
    while j > left and arr[j] > pivot:
      j -= 1
    if i < j:
      arr[i], arr[j] = arr[j], arr[i]
  if arr[i] > pivot:
    arr[i], arr[right] = arr[right], arr[i]
  return i
    





arr = [22, 11, 86, 66, 55, 77, 33, 44]
quick_sort(arr, 0, len(arr) - 1)
print(arr)