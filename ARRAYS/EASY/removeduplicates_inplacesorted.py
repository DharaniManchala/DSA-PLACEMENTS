class Solution:
    def removeduplicates(self,nums):
        unique_set=set(nums)
        k=len(unique_set)
        index=0
        for i in unique_set:
            nums[index]=i
            index+=1
        return k
# Example usage:
if __name__=="__main__":
    sol=Solution()
    nums=[1,1,2,2,3,4,4,5]
    k=sol.removeduplicates(nums)
    print("Number of unique elements:",k)

# time complexity: O(n) where n is the number of elements in the array
# space complexity: O(n) due to the set used to store unique elements

# optimal approach
class Solution:
    def removeduplicates(self,nums):
        if not nums:
            return 0
        i=0
        for j in range(1,len(nums)):
            if nums[j]!=nums[i]:
                i+=1
                nums[i]=nums[j]
        return i+1
# Example usage:
if __name__=="__main__":
    sol=Solution()
    nums=[1,1,2,2,3,4,4,5]
    k=sol.removeduplicates(nums)
    print("Number of unique elements:",k)
# time complexity: O(n) where n is the number of elements in the array
# space complexity: O(1) since we are using only a constant amount of extra space