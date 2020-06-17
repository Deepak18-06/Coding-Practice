'''
# this code is for recursive solution for the fibanacci series
def fibDp(n):
    if n <= 1:
        print(n)
        return n
    else:
        return (fibDp(n-1)+fibDp(n-2))
fibDp(5)
'''
def fib(n,lookup):
    # the base case
    if n == 1 or n == 0:
        lookup[n] = n
    # cal the lookup if  not calculated
    if lookup[n] is None:
        lookup[n] = fib(n-1,lookup) + fib(n-2,lookup)
    return lookup[n]
        