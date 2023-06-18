# 2^0, 2^1 , 2^2 ........ 1,2,4,8,12, ...... multiplication serious:
# ----------------------------recursion---------------------------------------


def powerOfTwo(n):
    if n == 0:   # ****this is the base condition for stopping the recursion.
        return 1
    else:
        result = powerOfTwo(n-1)
        return result*2

print(powerOfTwo(10))














# ----------------------Iteration:-------------------

# def power2(n):
#     # assert int(n) == n and n >= 0 , "Number should be posiive"
#     result=1
#     for i in range(1,n+1):
#         result = result*2 # left side assign value in to variable  after completing math equation into right side = Math equation complete in right side firt then assing value to left side.   
        
#     return result
    

# print(power2(3))

# ------------------------------------
# def power2(n):
#     i = 0
#     power = 1
#     while i<n:
#         power = power*2
#         i+=1
#     return power

# print(power2(10))     