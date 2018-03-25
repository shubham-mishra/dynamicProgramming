#fibonaci using recursive with memoization

def fib_memo(n):
    memo = [None] * (n+1);
    return fib(n, memo)

def fib(n, memo):
    if memo[n] is not None:
        return memo[n]
    else:
        if n == 1 or n == 2:
            result =  1;
        else:
            result = fib(n-1,memo) + fib(n-2,memo)
        memo[n] = result;
        return result;
     
print( fib_memo(4) )


#fibonaci using back propogation

def fib(n):
    memo = [None] * (n+1)
    memo[1] = memo[2] = 1
    
    for i in range(3,n+1):
        memo[i] = memo[i-1] + memo[i-2];
    
    return memo[n]
    
print(fib(32))