# it'a divided and conqure sorting Algorithm:

# ----------------------devided and conqure process---------------------
# 1. merge(arr):
# 2.  if len(arr) <= 1
# 3.      return 

# 4. mid = len(arr)// 2  =>[// if use , then not return float number]

# 5.left = arr[:mid] => arr[0 to mid]
# 6.right = arr[mid:]  => arr[mid to end]

# 7. call the => merge(arr) function again , for recursive here... and devided + conqure method
# ----------------------------------------------
# ----------------------------------------------
# 8. merge(left) 
# 9. merge(right)
# --------------------------------------------
# 10. call the merge_tow_sorted_lists(left, right,arr)
# ----------------------------------------------------
# ----------------------------------------------------

# ------------------------------------------------------
# -----------------------start the sort of merge element:-------------------------------
# 11. sort those element by call merge_tow_sorted_lists(left,right,arr)

# merge_tow_sorted_lists(a,b,arr):

# len_a = len(a)
# len_b = len(b)

# i = 0 => for iterate  ->a    ;(array[i]);
# j = 0 => for iterate  ->b    ;(array[j]);
# k = 0 => for iterate and store the sorted elements in array[k].

# i = j = k = 0

#         while i < len_a and j < len_b:
#             if a[i] <= b[j]:
#                 arr[k] = a[i]
#                 i+=1
#                  k+=1
#             else:
#                 arr[k] = [j]
#                 j+=1
#                  k+=1
            
#         while(i <len_a):
#             arr[k] = a[i]
#             i+=1 
#             k+=1
        
#         while(j <len_b):
#             arr[k] = a[j]
#             j+=1
#             k+=1
# ------------------------------------------------------
# ------------------------------------------------------


def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, arr)

def merge_two_sorted_lists(a,b,arr):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i+=1
            k+=1
        else:
            arr[k] = b[j]
            j+=1
            k+=1
        

    while i < len_a:
        arr[k] = a[i]
        i+=1
        k+=1

    while j < len_b:
        arr[k] = b[j]
        j+=1
        k+=1


#-------------------end algorithm--------------------------

list = [10,3, 3, 15, 7, 8, 23, 98, 29]
merge_sort(list)
print(list)

# if __name__ == '__main__':
#     test_cases = [
#         [10, 3, 15, 7, 8, 23, 98, 29],
#         [],
#         [3],
#         [9,8,7,2],
#         [1,2,3,4,5]
#     ]

#     for arr in test_cases:
#         merge_sort(arr)
#         print(arr)



