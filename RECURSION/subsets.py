class Solution:
    def Subsets(self,nums):
        result=[]
        def backtrack(index,current):
            if index==len(nums):
                result.append(current[:])
                return
            #include
            current.append(nums[index])
            backtrack(index+1,current)
            #exclude
            current.pop()
            backtrack(index+1,current)
        backtrack(0,[])
        return result
# Example usage:
nums=[1,2,3]
solution=Solution()
print(f"The subsets of {nums} are: {solution.Subsets(nums)}")
# time complexity: O(2^n) since each element can either be included or excluded, leading to 2^n possible subsets
# space complexity: O(n) due to the maximum depth of the recursion stack being n in the worst case when all elements are included in the current subset.