class Solution:
    def length_of_substring(self,s):
        n=len(str)
        maxlen=0
        for i in range(n):
            hashset=[0]*256
            for j in range(i,n):
                if hashset[ord(str[j])]==1:
                    break
                hashset[ord(str(j))]=1
                current_len=j-i+1
                maxlen=max(maxlen,current_len)
        return maxlen

if __name__=="__main__":
    s="abcabbabc"
    sol=Solution()
    print(sol.length_of_substring(s))
# Time complexity: O(n^2)
# Space complexity: O(1)



