'''Implementing the insertion sort algorithim'''

def insertion_sort(list_a):
  indexing_length = range(1, len(list_a))
  for i in indexing_length:
    value_to_sort = list_a[i] # get value to sort

    # compare to item to its left -> if left item greater swap
    while list_a[i - 1] > value_to_sort and i > 0:
      list_a[i], list_a[i - 1] = list_a[i - 1], list_a[i]
      i = i - 1

  return list_a


print(insertion_sort([44,6,32,5,23,1,456]))

