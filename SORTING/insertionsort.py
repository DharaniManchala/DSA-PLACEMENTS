class Solution:
    def insertionsort(self,nums):
        n=len(nums)
        for i in range(1,n):
            key=nums[i]
            j=i-1
            while j>=0 and nums[j]>key:
                nums[j+1]=nums[j]
                j-=1
            nums[j+1]=key
        return nums
# Example usage:
if __name__=="__main__":
    sol=Solution()
    nums=[12,11,13,5,6]
    sorted_nums=sol.insertionsort(nums)
    print("Sorted array is:", sorted_nums)

    # time complexity: O(n^2) where n is the number of elements in the array
    # space complexity: O(1) since we are sorting the array in place without using any additional data structures


    