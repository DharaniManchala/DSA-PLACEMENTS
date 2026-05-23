class Solution:
    def search(self,target,nums):
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return left
# Example usage:
if __name__=="__main__":
    sol=Solution()
    nums=[1,3,5,6]
    target=2
    result=sol.search(target,nums)
    print("Target should be inserted at index:", result)

    # time complexity: O(log n) where n is the number of elements in the array
    # space complexity: O(1) since we are using only a constant amount of extra space
