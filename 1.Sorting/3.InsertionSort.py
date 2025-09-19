#insersion Sort:
# ----------------
# 1. start outerLoop (1,len(array))
# 2. value = index1 , store value of index 1 to -> value
# 3. i = index-1 , previous element for comparing element right side to left side index.... i will be dicrement. 
# 4. while (i>=0) , then continue
# 5. if (value < list[i]) , here -> list[i] = 0 index ... if previouse element gretter then next element.
# 6. list[i+1] = list [i] , then store the big number to the next index.
# 7. list[i] = value , store the small number to the list[i].
# 8. i = i-1 , goto left next index for comparing the element.


def insertion(array):
    for  index in range(1,len(array)):
        value = array[index]
        i = index-1
        while(i>=0):
            if(value<array[i]):
                array[i+1]=array[i]
                array[i]=value
                i=i-1
            else:
                break

# another code:
# def insertionSort(array):

#     for step in range(1, len(array)):
#         key = array[step]
#         j = step - 1
        
#         # Compare key with each element on the left of it until an element smaller than it is found
#         # For descending order, change key<array[j] to key>array[j].        
#         while j >= 0 and key < array[j]:
#             array[j + 1] = array[j]
#             j = j - 1
        
#         # Place key at after the element just smaller than it.
#         array[j + 1] = key

array=[3,45,65,1,3,6,4]
insertion(array)
print(array)
