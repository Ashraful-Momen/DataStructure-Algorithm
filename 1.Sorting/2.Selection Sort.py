# selectionSort(array, size)
#   repeat (size - 1) times
#   set the first unsorted element as the minimum
#   for each of the unsorted elements
#     if element < currentMinimum
#       set element as new minimum
#   swap minimum with first unsorted position
# end selectionSort
# ----------------------------------------------

#Selection Sort: 
# --------------------

def selectionSort(array,size):

    for first_index in range(size): # step : 0,1,2,3.... cz range interate as range(0,size)
        min_index = first_index # so then min_index will be : 0 then 1,2,3,.....
        for j in range(first_index+1,size):
            if array[j]<array[min_index]:
                min_index = j
        
        (array[first_index], array[min_index]) = (array[min_index], array[first_index])



data = [-2, 45, 0, 11, -9]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)



