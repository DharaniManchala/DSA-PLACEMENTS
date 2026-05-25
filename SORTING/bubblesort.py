class Solution:
    def bubblesort(self,nums):
        n=len(nums)
        for i in range(n):
            for j in range(0,n-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        return nums
# Example usage:
if __name__=="__main__":
    sol=Solution()
    nums=[64,34,25,12,22,11,90]
    sorted_nums=sol.bubblesort(nums)
    print("Sorted array is:", sorted_nums)

    # time complexity: O(n^2) where n is the number of elements in the array
    # space complexity: O(1) since we are sorting the array in place without using any additional data structures