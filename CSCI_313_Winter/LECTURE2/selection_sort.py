'''Implementing the selection sort algorithim'''
# first num = min
# search for new min
# min value moved to left
# divide list into 2 sublists 
# left will be sorted right wont
# continue the checks until we get to the end of the list

def selection_sort(list_a):
  # -1 because we dont need to compare the last item because we can assume last item will be the highest
  indexing_length = range(len(list_a) - 1) 
  
  for i in indexing_length:
    min_value = i

    for j in range(i + 1, len(list_a)):
      # if next val is less than current smallest make min value hold its index
      if list_a[j] < list_a[min_value]:
        min_value = j
    
    # if the minimum value changed swap with the first value i
    if min_value != i:
      list_a[min_value], list_a[i] = list_a[i], list_a[min_value]
  return list_a

items = [4, 6, 2, 8, 7]
print(selection_sort(items))
  