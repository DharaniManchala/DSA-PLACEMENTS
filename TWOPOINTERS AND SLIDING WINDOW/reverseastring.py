# using two pointers approach
class Solution:
    def reversestring(self,s):
        left=0
        right=len(s)-1
        while left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        return s
if __name__ == "__main__":   
    s=["h","e","l","l","o"]
    print(Solution().reversestring(s))
    # Output: ["o","l","l","e","h"]
    # time complexity is O(n) and space complexity is O(1)