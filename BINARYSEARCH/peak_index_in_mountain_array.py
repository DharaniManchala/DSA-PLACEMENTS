class Solution:
    def peakindex(self,nums):
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]<nums[mid+1]:
                left=mid+1
            else:
                right=mid
        return left
# Example usage:
if __name__=="__main__":
    sol=Solution()
    nums=[0,1,0]
    peak_index=sol.peakindex(nums)
    print("Peak index in the mountain array:", peak_index)

    # time complexity: O(log n) where n is the number of elements in the array
    # space complexity: O(1) since we are using only a constant amount of extra space
