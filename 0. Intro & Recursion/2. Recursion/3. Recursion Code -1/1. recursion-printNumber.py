#Recursive Function is mantain the stack data structure: (LIFO)

def r_f(n):
    if n<1:
        print("N is less than 1")
    else: 
        r_f(n-1)
        print(n)
        
r_f(4)

