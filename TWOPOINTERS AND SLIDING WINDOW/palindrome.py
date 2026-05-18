class Solution:
    def palindrome(sself,s):
        left=0
        right=len(s)-1
        while left<right:
            while left<right and not s[left].isalnum():
                left+=1
            while left<right and not s[right].isalnum():
                right-=1
            if s[left].lower()!=s[right].lower():
                return False
            left+=1
            right-=1
        return True
if __name__ == "__main__":
    s="A man, a plan, a canal: Panama"
    print(Solution().palindrome(s))
    # Output: True
    # time complexity is O(n) and space complexity is O(1)

        