#Quick Sort is a stable but merge is not stable 

> take last number from array as pivot. [we can select pivot any num from arr but best is the last index of array]

> compare number with pivot , 
    
    > if the number is smaller than pivot , then put the number in left side in the array . 

    > if the number is bigger or equal than pivot , then put the number in right side in the array . 



# array = [10,3,1,80,33,7,4,2]
# Quick Sort = [1,2,3,4,7,q->10,33,80] # [smaller number , quicksort element , big number ]

#partition:-------------------partition(array,l,h):
# let i = l
# let j = h
# 1.pivot = could be any number of array , first number or last number or any random number but we consider pivot as index[0=i]
# 2.lowest number => i= l ,number.
# 3.hieght number =>  j = h ,number. if (i<j) then run while loop
# 4.i=array[0], check right side element as i<=pivot , then i++ , if i found big number then pivot (i>pivot), then i stop on the index.
# 5.j=array[len(array)-1], last index. check the number with pivot as j>pivot, if found smaller number then , j stop on index of array . 
# 6. let i get big number and j get smaller number and (i>j) then pivot , then swap(array[i],array[j]).if(i not = j)
# 7. then continue for checking number  from i and j , where stopped.
# 8. if the whileLoop condition break then , swap(array[l]=0, array[j]...'the last value of j (midvalue)') , cz after whileLoop j will be small number < pivot. and then swap().
# 9. return j.

#QuickSort:---------------------quicksort(array,l,h):
# let i = l
# let j = h
# 1.if(l<h) or (i<j):
#   j = partition(array,l,h) , which is return J=pivotElement. [1,2,3,4,7,j->10,33,80] 
#   quicksort(array,l,j) -> left side array , which all small number then pivot. [1,2,3,4,7]
#   quicksort(array,j+1,h) -> left side array , which all big number then pivot.[33,80] 


# --------------------Maint code i : -------------------

# chatgpt:------------------------------- i = start_index[0] and j=[endIndex]
# def swap(array, i, j):   
#     if i != j:
#         temp = array[i]
#         array[i] = array[j]
#         array[j] = temp

# def quicksort(array, i, j):
#     if i < j:
#         pivot = partition(array, i, j)
#         quicksort(array, i, pivot)  # Exclude pivot element from the subsequent calls
#         quicksort(array, pivot + 1, j)  # Include pivot element in the subsequent calls

# def partition(array, i, j):
#     pivot_index = i
#     pivot = array[pivot_index]

#     while i < j:
#         while i < len(array) and array[i] <= pivot:
#             i += 1
#         while array[j] > pivot:
#             j -= 1

#         if i < j:
#             swap(array, i, j)

#     swap(array, pivot_index, j) #pivot swapping here. and pivot fixed in middle of the array.(i=big then pivot , j=small then pivot , just exchange the  j last index value of array with pivot element)

#     return j

# array = [100,11, 9, 29, 7, 2, 15, 28]
# quicksort(array, 0, len(array) - 1)
# print(array)


  


#chat gpt code : -----------------
# procedure swap(elements, start, end):
#     if start != end:
#         temp = elements[start]
#         elements[start] = elements[end]
#         elements[end] = temp

# procedure quicksort(elements, start, end):
#     if start < end:
#         pivot = partition(elements, start, end)
#         quicksort(elements, start, pivot)    // Exclude pivot element from subsequent calls
#         quicksort(elements, pivot + 1, end)  // Include pivot element in subsequent calls

# function partition(elements, start, end):
#     pivot_index = start
#     pivot = elements[pivot_index]

#     while start < end:
#         while start < length(elements) and elements[start] <= pivot:
#             start += 1
#         while elements[end] > pivot:
#             end -= 1

#         if start < end:
#             swap(elements, start, end)

#     swap(elements, pivot_index, end)

#     return end

# elements = [11, 9, 29, 7, 2, 15, 28]
# quicksort(elements, 0, length(elements) - 1)
# print(elements)



#quick sort: more time practise--------------------------
def swap(array,i,j):
    if(i != j):
        tem = array[i]
        array[i]= array[j]
        array[j]=tem

def partition(array,i,j):
    pivot_index = i
    pivot = array[pivot_index]
    while i<j :
            
                while i<len(array) and array[i]<=pivot:
                    i+=1
                    
                while(array[j]>pivot):
                     j-=1
                if(i<j):
                    swap(array,i,j)
                
            
    swap(array,pivot_index,j)

    return j

def quicksort(array,i,j):
   
    if(i<j):
        pivot = partition(array,i,j)
        quicksort(array,i,pivot) # left side array
        quicksort(array,pivot+1,j) #right side array 



array= [101,11, 9, 29, 7, 2, 15, 28,0]

quicksort(array,0, len(array)-1)

print(array)


