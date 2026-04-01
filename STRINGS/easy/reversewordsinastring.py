class Solution:
    def reversewords(self,str):
        words=[]
        word=""
        for c in str:
            if c!=" ":
                word+=c
            elif word:
                words.append(word)
                word=""
        if word:
            words.append(word)
        words.reverse()
        return ' '.join(words)
# example usage:
if __name__=="__main__":
    sol=Solution()
    str="Hello World"
    result=sol.reversewords(str)
    print(result)  # Output: "World Hello"

    #time complexity: O(n) where n is the length of the input string
    #space complexity: O(n) in the worst case when all characters are non-space, otherwise O(1) if there are no words