class Solution:
    def removeoutermostparanthesis(self,str):
        result=[]
        depth=0
        for char in str:
            if char=='(':
                depth += 1
                if depth > 1:
                    result.append(char)
            elif char==')':
                depth -= 1
                if depth > 0:
                    result.append(char)
        return ''.join(result)
# example usage:
if __name__=="__main__":
    sol=Solution()
    str="(()())(())"
    result=sol.removeoutermostparanthesis(str)
    print(result)  # Output: "()()()"

    #time complexity: O(n) where n is the length of the input string
    #space complexity: O(n) in the worst case when all parentheses are nested, otherwise O(1) if there are no nested parentheses