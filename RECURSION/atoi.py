def atoi(s):
    if len(s)==1:
        return int(s)
    return atoi(s[:-1])*10+int(s[-1])
# Example usage:
print(atoi("1234"))  # Output: 1234
# Time Complexity: O(n) where n is the length of the string
# Space Complexity: O(n) due to the recursive call stack, where n is the length of the string