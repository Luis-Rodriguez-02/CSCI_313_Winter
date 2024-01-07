'''Implementing the binary search algorithm both recursivly and iteratively'''

# Search algorithim that finds the position of a target in a sorted array. Half of the array is eliminated during each step
def iter_binary_search(iterable, target):
  low, high = 0, len(iterable) - 1
  
  while low <= high: 
    middle = low + ((high - low) // 2)
    value = iterable[middle] 
    if value == target:
      return middle
    elif value > target:
      high = middle - 1
    else:
      low = middle + 1

  return -1
  
def recur_binary_search(iterable, target, low, high):
  
  if low <= high:
    mid = low + ((high - low) // 2)
  
    if iterable[mid] == target:
      return mid
    elif iterable[mid] > target:
      return recur_binary_search(iterable, target, low, mid - 1)
    elif iterable[mid] < target:
      return recur_binary_search(iterable, target, mid + 1, high)
  else:
    return -1


test_list = [5, 3, 9, 22, 40, 15]
sorted_list = sorted(test_list)
index = (recur_binary_search(sorted_list, 5, 0, len(sorted_list) - 1))

print(sorted_list)


if index == -1:
  print('Element doesn\'t exist in list')
else:
  print(f'Element found at index: {index}')
  print(sorted_list[index])


