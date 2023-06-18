import sys
sys.setrecursionlimit(10000)    # Increase the recursion limit in stack memory
def fact(n):
    assert n>=0 and int(n)==n , "The number should be positive integer"
    if n in [0,1]:
        return 1
    else:
        return n*(fact(n-1))

print(fact(-1.54))


# ===============================================
# def factorial(n):
#     assert int(n)==n and n>=0, "The number should be positive integer"
#     # if n<=0:
#     if n in [0,1]:
#         return 1
#     else:
#         return n*factorial(n-1)

# print(factorial(-4))
# --------------for loop-----------------


# fact(4)= 4*3*2*1

# def factorial(n):
# 	result = 1
# 	for i in range(1,n+1):
# 		result = result*i
        
# 	return result

# print(factorial(0))
# -------------while loop-----------------

# def factorial(n):
# 	result = 1
# 	i=1
# 	while i<=n:
# 		result*=i
# 		i+=1
# 	return result

# print(factorial(-1))



   