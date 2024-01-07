'''Implementing the bubble sort algorithim

- check if left value > right value
- if greater swap
- continue iterations until no swaps -> this means its sorted

'''

def bubble_sort(list_a):
  # python excludes the stop variable so i+1 will allow us to test the rightmost last var
  indexing_length = len(list_a) - 1 # 
  sorted = False

  while not sorted: # while True
  # we set sorted to true so that if on the last iteration the if statment doesn't run not (true) == false so loop breaks
    sorted = True 
    for i in range(0, indexing_length):
      if list_a[i] > list_a[i + 1]:
        sorted = False # set F to stay in loop
        list_a[i], list_a[i + 1] = list_a[i + 1], list_a[i]
  return list_a



unsorted_list = [10, 7, 3, 1, 2, 99, 50, 120, -1]
print(bubble_sort(unsorted_list))
    
    