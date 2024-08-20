'''
Given Fibonacci Sequence has F0=0 F1=1 and F(n)=F(n-1)+F(n-2)

Properties:- 
1. Cassini's identity:
    F(n-1)*F(n+1) - F(n)^2 = (-1)^n
2. Addition Rule:
    F(n+k) = F(k)*F(n+1) + F(k-1)*F(n)
    F(2n) = F(n)*(F(n+1) + F(n-1))

    From this we can say, if k is an integer then F(nk) is a multiple of F(n)
3. GCD identity:
    GCD(F(m), F(n)) = F_GCD(m,n)

    Fibonacci numbers are the worst possible inputs for Euclidean Algorithm (Lame's Theorem in Euclidean Algo)

    Mathematically F(n) can be derived as F(n) = (((1+sqrt(5))/2)^n - ((1-sqrt(5))/2)^n)/sqrt(5)
4. Matrix Form:
    (1 1)^n = (F(n+1) F(n))
    (1 0)     (F(n)   F(n-1))
'''

import time
# Function to measure time of execution
def m_time(func, *args, **kwargs):
    """
    Measure the time taken to execute a function.
    Parameters:
    func (callable): The function to be timed.
    *args: Arguments to pass to the function.
    **kwargs: Keyword arguments to pass to the function.
    Returns:
    The result of the function and the time taken.
    """
    start_time=time.time()
    result=func(*args, **kwargs)
    end_time=time.time()
    exec_time=end_time-start_time
    print(f"Time taken: {exec_time:.10f} secs")
    return result

# Fibonacci in O(n!):- Simple Recursion
def F_Recursion(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n<0:
        return 'Invalid Input'
    else:
        return (F_Recursion(n-1) + F_Recursion(n-2))




# Fibonacci in O(n):- Using DP
def F_DP(n):
    if n<0:
        return 'Invalid Input'
    elif n==0:
        return 0
    elif n==1:
        return 1
    a=0
    b=1
    for x in range(2,n+1):
        t = a+b
        a = b
        b = t
    return b


# Fibonacci in O(log(n)):- Using Binary Exponentiation and Matrix
def F_BinExp(n):
    if n<0:
        return 'Invalid Input'
    elif n==0:
        return (0,1)
    
    p = F_BinExp(n>>1)
    c = p[0]*(2*p[1]-p[0])
    d = p[0]*p[0] + p[1]*p[1]

    if(n&1):
        return(d,c+d)
    else:
        return(c,d)


n = int(input())
'''
r = m_time(F_Recursion,n)
print(f"F({n})={r} in Recursion Method")
'''
r = m_time(F_DP,n)
print(f"F({n})={r} in DP Method")

r = m_time(F_BinExp,n)
print(f"F({n})={r[0]} in Binary Exponentiation and Matrix Method")