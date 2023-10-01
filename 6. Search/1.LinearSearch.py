

def search(num,list):
    i = 0
    while (i<len(list)):

        if num == list[i]:
            return print(f'fount {num} at index: {i}')
        
        i+=1
    return print(f'not Found')
   



  
if __name__ == '__main__':

    list = [1,2,3,4,5,6]
    num = 100

    search(num,list)

   