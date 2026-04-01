class Solution:
    def largestelement(self,nums):
        largest=nums[0]
        for num in nums:
            if num>largest:
                largest=num
        return largest
    
# Example usage:
solution=Solution()
nums=[3,1,4,1,5,9]
print(solution.largestelement(nums))

# time complexity: O(n) where n is the number of elements in the array
# space complexity: O(1) since we are using only a constant amount of extra space