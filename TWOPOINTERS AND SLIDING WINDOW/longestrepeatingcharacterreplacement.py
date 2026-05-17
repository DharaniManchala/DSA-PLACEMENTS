class Solution:
    def longestrepeatingcharacters(self,s,k):
        left=0
        maxf=0
        maxlength=0
        hashmap={}
        for right in range(len(s)):
            ch=s[right]
            hashmap[ch]=hashmap.get(ch,0)+1
            maxf=max(maxf,hashmap[ch])
            while (right-left+1)-maxf>k:
                leftch=s[left]
                hashmap[leftch]-=1
                left+=1
            maxlength=max(maxlength,right-left+1)
        return maxlength
# example usage
if __name__=="__main__":
    sol=Solution()
    s="AABABBA"
    k=1
    print(sol.longestrepeatingcharacters(s,k))
    # time complexity: O(n) where n is the length of the input string, since we are iterating through the string once
    # space complexity: O(1) since we are using only a constant amount of extra space for the hashmap, which can have at most 26 entries for uppercase letters
