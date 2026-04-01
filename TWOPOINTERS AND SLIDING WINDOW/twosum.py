class Solution:
    def twosum(self,nums,target):
        hashmap={}
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in hashmap:
                return [hashmap[complement],i]
            hashmap[nums[i]]=i
        return []
# example usage
if __name__=="__main__":
    sol=Solution()
    nums=[2,7,11,15]
    target=9
    result=sol.twosum(nums,target)
    print(result)  # Output: [0, 1]

    #time complexity: O(n) where n is the number of elements in the array
    #space complexity: O(n) since we are using a hashmap to store the indices of the elements
