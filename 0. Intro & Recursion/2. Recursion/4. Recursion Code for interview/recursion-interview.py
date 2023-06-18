# The sum of Digit: 
def SumOfDigit(n):
    assert n>=0 and int(n)==n, "Input value should be positive integer"
    if n==0:
        return 0
    else:
        return int(n%10) + SumOfDigit(n/10)
    
ans=SumOfDigit(333)
print(ans)
# =====================================================
#Power of Digit:
def PowerOfDigit(base,expo):
    assert expo>=0 and int(expo)==expo, "Exponent Should be positive integer"
    if expo == 0:
        return 1 
    elif expo == 1:
        return base
    else:
        return base*PowerOfDigit(base,expo-1)

ans=PowerOfDigit(2,4)
print(ans)
# ======================================================
#GCD by Recursion Funciton:
def gcd(a,b):
    assert int(a) == a and int(b) == b, "a and b should be integer!"
    if a<0:
        a = -1 * a 
    elif b<0:
        b = -1 * b
    elif b==0:
        return a
    else:
        return gcd(b,a%b)
print(gcd(48,18))
# ===================================================
#Decimal to Binary:
def DecimalToBinary(n):
    assert int(n)==n, "N should be positive integer"
    if n==0:
        return 0
    else:
        return n%2 + 10 * DecimalToBinary(int(n/2))

print(DecimalToBinary(4))