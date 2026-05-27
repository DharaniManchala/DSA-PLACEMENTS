def factorial(n):
    if n<0:
        return "Factorial is not defined for negative numbers"
    elif n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
# Example usage:
n=5
print(f"The factorial of {n} is: {factorial(n)}")
# time complexity: O(n) since each call to factorial(n) results in one additional call to factorial(n-1) until it reaches the base case
# space complexity: O(n) due to the maximum depth of the recursion stack being n in the worst case when n is large.