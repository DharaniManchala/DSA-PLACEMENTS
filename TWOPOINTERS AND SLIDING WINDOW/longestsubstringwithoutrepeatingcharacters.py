# class Solution(object):

#     def lengthOfLongestSubstring(self, s):

#         hashmap = {}

#         left = 0
#         maxcount = 0

#         for right in range(len(s)):

#             ch = s[right]

#             hashmap[ch] = hashmap.get(ch, 0) + 1

#             # keep shrinking until valid
#             while hashmap[ch] > 1:

#                 leftch = s[left]

#                 hashmap[leftch] -= 1

#                 if hashmap[leftch] == 0:
#                     del hashmap[leftch]

#                 left += 1

#             maxcount = max(maxcount, right - left + 1)

#         return maxcount
# # example usage
# if __name__ == "__main__":
#     sol = Solution()
#     s = "abcabcbb"
#     print(sol.lengthOfLongestSubstring(s))
#     # time complexity: O(n) where n is the length of the input string, since we are iterating through the string once
#     # space complexity: O(1) since we are using only a constant amount of extra space for the hashmap


class Solution:
    def lengthoflongestsubstring(self,s):
        left=0
        maxcount=0
        charset=set()
        for right in range(len(s)):
            ch=s[right]
            while ch in charset:
                leftch=s[left]
                charset.remove(leftch)
                left+=1
            charset.add(ch)
            maxcount=max(maxcount,right-left+1)
        return maxcount
# example usage
if __name__=="__main__":
    sol=Solution()
    s="abcabcbb"
    print(sol.lengthoflongestsubstring(s))
    # time complexity: O(n) where n is the length of the input string, since we are iterating through the string once
    # space complexity: O(1) since we are using only a constant amount of extra space for the charset set
    