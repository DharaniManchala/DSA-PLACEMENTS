class Solution:
    def removeoutermostparaenthesis(self,s):
        result="" 
        count=0
        for char in s:
            if char=="(":
                if count>0:
                    result+=char
                count+=1
            else:
                count-=1
                if count>0:
                    result+=char
        return result
# example usage:
if __name__=="__main__":
    sol=Solution()
    s="(()())(())"
    print(sol.removeoutermostparaenthesis(s))  # Output: "()()()"

    #time complexity: O(n) where n is the length of the input string
    #space complexity: O(n) for storing the result string in the worst case when all parentheses are nested.