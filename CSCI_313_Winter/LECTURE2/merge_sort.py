'''Implementing merge sort
- divide and conquer aglo
- break down proboelm into multiple sub-prolems recursively until they become simple to solve
- solutions are combined to solve original problem
- O(nlogn) runtime
'''

# 1 - split array in half
# 2 - call merge sort on each half to split recursively
# 3 - merge both sorted halves into one sorted array
# consider left over elements
def merge_sort(arr):
    
    if len(arr) > 1:
    # split the array into two halves
      left_arr = arr[:len(arr) // 2]
      right_arr = arr[len(arr) // 2:]

      merge_sort(left_arr)
      merge_sort(right_arr)

      i, j, k = 0, 0, 0  # i -> left arr index, j -> right arr index, k -> original arr index

      while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
          arr[k] = left_arr[i]
          i += 1  # increment index of left arr to not consider value placed in original arr
        else:
          arr[k] = right_arr[j]
          j += 1  # increment index of right arr to not consider value placed in original arr
        k += 1

      # now consider cases where original array was odd and the while condition was broken because un-equal left or right array lengths
      
      # if left array has elements left
      while i < len(left_arr):
          arr[k] = left_arr[i]
          i += 1
          k += 1
      
      while j < len(right_arr):
          arr[k] = right_arr[j]
          j += 1
          k += 1
    return arr  
    
      


arr_test = [4,3,7,8,9,10]

print(merge_sort(arr_test))
print(arr_test)    
    
