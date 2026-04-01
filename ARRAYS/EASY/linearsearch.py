class Solution:
    def linearsearch(self,nums,target):
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        return -1
# Example usage:
if __name__=="__main__":
    sol=Solution()
    nums=[1,2,3,4,5]
    target=3
    print(sol.linearsearch(nums,target))  # Output: 2

    #time complexity: O(n) where n is the number of elements in the array
    #space complexity: O(1) since we are using only a constant amount of extra space