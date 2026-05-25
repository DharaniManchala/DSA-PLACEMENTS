class Solution:
    def selectionsort(self,nums):
        n=len(nums)
        for i in range(n):
            minindex=i
            for j in range(i+1,n):
                if nums[j]<nums[minindex]:
                    minindex=j
            nums[i],nums[minindex]=nums[minindex],nums[i]
        return nums
# Example usage:
if __name__=="__main__":
    sol=Solution()
    nums=[64,25,12,22,11]
    sorted_nums=sol.selectionsort(nums)
    print("Sorted array is:", sorted_nums)

    # time complexity: O(n^2) where n is the number of elements in the array
    # space complexity: O(1) since we are sorting the array in place without using any additional data structures