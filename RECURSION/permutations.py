class Solution:
    def permute(self,nums):
        result=[]
        def backtrack(i):
            if i==len(nums):
                result.append(nums[:])
                return
            for j in range(i,len(nums)):
                nums[i],nums[j]=nums[j],nums[i]
                backtrack(i+1)
                nums[i],nums[j]=nums[j],nums[i]

        backtrack(0)
        return result
# example usage
if __name__=="__main__":
    sol=Solution()
    nums=[1,2,3]
    result=sol.permute(nums)
    print(result)  # Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]

    #time complexity: O(n*n!) where n is the number of elements in the array
    #space complexity: O(n) for the recursion stack and O(n!) for storing the results
        