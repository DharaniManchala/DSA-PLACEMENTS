class Solution:
    def maximumsubarraysum(self,nums,k):
        maxsum=0
        for i in range(len(nums)-k+1):
            window=nums[i:i+k]
            if len(set(window))==k:
                maxsum=max(maxsum,sum(window))
        return maxsum
# Example usage:
if __name__=="__main__":
    solution=Solution()
    nums=[1,2,3,4,5]
    k=3
    result=solution.maximumsubarraysum(nums,k)
    print("Maximum sum of distinct subarrays with length",k,"is:",result)

    #time complexity: O(n*k) where n is the length of the input array and k is the length of the subarray.
    #space complexity: O(k) for the set used to check distinct elements in the subarray.