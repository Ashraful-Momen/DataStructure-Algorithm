def power2(n):
    # assert int(n) == n and n >= 0 , "Number should be posiive"
    if n==0:
        return 2
    result=1
    for i in range(1,n+1):
        result = 2*i
    return result
    

print(power2(10))
        