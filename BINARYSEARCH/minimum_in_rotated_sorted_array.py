class Solution:
    def minimum_in_rotated_sorted_array(self,nums):
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]>nums[right]:
                left=mid+1
            else:
                right=mid
        return nums[left]
# Example usage:
if __name__=="__main__":
    sol=Solution()
    nums=[3,4,5,1,2]
    minimum_element=sol.minimum_in_rotated_sorted_array(nums)
    print("Minimum element in the rotated sorted array:", minimum_element)

    # time complexity: O(log n) where n is the number of elements in the array
    # space complexity: O(1) since we are using only a constant amount of extra space