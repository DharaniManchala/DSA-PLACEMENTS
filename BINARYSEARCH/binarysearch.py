class Solution:
    def binarysearch(self,nums,target):
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
        return -1
# example
if __name__=="__main__":
        sol=Solution()
        nums=[-1,0,3,5,9,12]
        target=9
        print(sol.binarysearch(nums,target))  # Output: 4

    #time complexity: O(log n) where n is the number of elements in the array
    #space complexity: O(1) since we are using only a constant amount of extra space