class Solution:
    def twosum(self,nums,target):
        hashmap={}
        for i,num in enumerate(nums):
            complement=target-num
            if complement in hashmap:
                return [hashmap[complement],i]
            hashmap[num]=i
# Example usage:
if __name__=="__main__":
    sol=Solution()
    nums=[2,7,11,15]
    target=9
    print(sol.twosum(nums,target))  # Output: [0, 1]

    #time complexity: O(n)
    #space complexity: O(n)
