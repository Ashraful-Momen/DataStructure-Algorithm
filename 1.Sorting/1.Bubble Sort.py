#Bubble Sort:
# ------------
def bubbleSort(array):
   for x in range(len(array)):
       for y in range(0,len(array)-1-x):
           if(array[y]>array[y+1]):
               tem = array[y]
               array[y] = array[y+1]
               array[y+1] = tem

array = [3,2,1,0]
bubbleSort(array)
sortedArray = array

# print(array)
print(sortedArray)