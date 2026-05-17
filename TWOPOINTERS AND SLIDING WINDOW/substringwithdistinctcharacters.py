class Solution:
    def substringwithdistinctcharacters(self,s):
        left=0
        count=0
        hashmap={}
        for right in range(len(s)):
            ch=s[right]
            hashmap[ch]=hashmap.get(ch,0)+1
            if right-left+1>3:
                leftch=s[left]
                hashmap[leftch]=hashmap[leftch]-1
                if hashmap[leftch]==0:
                    del hashmap[leftch]
                left+=1
            if right-left+1==3 and len(hashmap)==3:
                count+=1
        return count
# example usage
if __name__=="__main__":
    sol=Solution()
    s="xyzzaz"
    print(sol.substringwithdistinctcharacters(s))
    # time complexity: O(n) where n is the length of the input string
    # space complexity: O(1) since we are using only a constant amount of extra
