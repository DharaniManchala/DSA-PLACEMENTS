def fib(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
# Example usage:
n=10
print(f"The {n}th Fibonacci number is: {fib(n)}")
# time complexity: O(2^n) since each call to fib(n) results in two additional calls to fib(n-1) and fib(n-2)
# space complexity: O(n) due to the maximum depth of the recursion stack being n in