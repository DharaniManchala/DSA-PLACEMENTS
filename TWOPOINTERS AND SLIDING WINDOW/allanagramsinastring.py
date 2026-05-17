class Solution:
    def allanagrams(self,s,p):
        count=0
        pcount={}
        scount={}
        for ch in p:
            pcount[ch]=pcount.get(ch,0)+1
        left=0
        for right in range(len(s)):
            ch=s[right]
            scount[ch]=scount.get(ch,0)+1
            if right-left+1>len(p):
                leftch=s[left]
                scount[leftch]=scount[leftch]-1
                if scount[leftch]==0:
                    del scount[leftch]
                left+=1
            if right-left+1==len(p) and scount==pcount:
                count+=1
        return count
if __name__=="__main__":
    sol=Solution()
    s="forxxorfxdofr"
    p="for"
    print(sol.allanagrams(s,p))
    # time complexity: O(n) where n is the length of the input string s, since we are iterating through the string once
    # space complexity: O(1) since we are using only a constant amount of extra


