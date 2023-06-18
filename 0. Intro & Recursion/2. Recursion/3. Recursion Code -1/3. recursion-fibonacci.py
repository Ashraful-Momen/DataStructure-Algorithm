# -----------------------------
def fibonacci(n):
    assert int(n)==n and n<=0 , "Input number should be positive for fibonacci"
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

n = int(input("Enter number of terms:"))
print("Fibonacci sequence:")
for i in range(n):
    print(fibonacci(i))
# --------------------------------------------
# def fibonacci(n):
#     assert int(n)==n and n>=0 , "Input number should be positive for fibonacci"
#     # if n==0 or n==1:
#     if n in [0,1]:
#         return n
#     else: 
#         return fibonacci(n-1)+fibonacci(n-2)

# print(fibonacci(4))

# -----------------------------



#---------------------fibo with :while Loop -----------------------

# def fibonacci(n):
#     first = 0
#     second = 1
#     count = 0
  
    
#     while count < n:
#         if count <= 1:
#             fibo = count
#         else:
#             fibo = first + second
#             first = second
#             second = fibo
#             # print(fibo)
        
#         count += 1
#         print(fibo)

#     return fibo

# # print(fibonacci(5))
# fibonacci(5)

# -------------------------for Loop-----------------
# def fibonacci(n):
#     assert int(n) == n and n >= 0, "fibonacci should be a non-negative integer"
    
#     if n == 0:
#         return 0

#     first = 0
#     second = 1
    
#     for count in range(n):
#         if count <= 1:
#             fibo = count
#         else:
#             fibo = first + second
#             first = second
#             second = fibo
        
#     return fibo

# print(fibonacci(-1))
# ========================================================



