class Solution:
    def first(self,nums,target):
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                first=mid
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return first
    def last(self,nums,target):
        n=len(nums)
        left=0
        right=n-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                last=mid
                left=mid+1
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return last
# Example usage:
if __name__=="__main__":
    sol=Solution()
    nums=[5,7,7,8,8,10]
    target=8
    first_position=sol.first(nums,target)
    last_position=sol.last(nums,target)
    print("First position of target:", first_position)
    print("Last position of target:", last_position)

    # time complexity: O(log n) where n is the number of elements in the array
    # space complexity: O(1) since we are using only a constant amount of extra space
    
