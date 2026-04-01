class Solution:
    def removeduplicatesfromsortedarray(self,nums):
        if len(nums)==0:
            return 0
        slow=0
        for fast in range(1,len(nums)):
            if nums[fast]!=nums[slow]:
                slow+=1
                nums[slow]=nums[fast]
        return slow+1
# example usage
if __name__=="__main__":
    sol=Solution()
    nums=[1,1,2,2,3,4,4,5]
    new_length=sol.removeduplicatesfromsortedarray(nums)
    print(new_length)  # Output: 5
    print(nums[:new_length])  # Output: [1, 2, 3, 4, 5]

    #time complexity: O(n) where n is the number of elements in the array
    #space complexity: O(1) since we are using only a constant amount of extra space
    

