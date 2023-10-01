list = [1,2,3,4,5,6,7,8,9]
item = 5


left = 0
right = len(list)-1



while left <= right:

    mid = (left+right)//2 

    if (list[mid]==item): 
        print(f'Item {item} found at : {list[mid]-1}')
        exit()

    elif (item>list[mid]):
        left = mid+1

    else: 
        right = mid-1
    
print(f'{item} not found')