def fibonacci(num):
    
   if num ==0:
       return 0
   if num ==1 :
       return 1
   else:
        return fibonacci(num-1) + fibonacci(num-2)
     
n = 6
result = fibonacci(n)
print(result)


def fibonacci_tabulation(n):
    if n <= 1:
        return n
    
    fib_table = [0] * (n + 1)
    
   
    fib_table[0] = 0
    fib_table[1] = 1
    
   
    for i in range(2, n + 1):
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]
    
    return fib_table[n]


n = 6 
result = fibonacci_tabulation(n)
print(result)


def fibonacci_memo(num, memo=None):
   
    if memo is None:
        memo = {}
    
    if num == 0:
        return 0
    if num == 1:
        return 1
    
    if num in memo:
        return memo[num]
    
    memo[num] = fibonacci_memo(num - 1, memo) + fibonacci_memo(num - 2, memo)
    
    return memo[num]

n = 10
result = fibonacci_memo(n)
print(result)
