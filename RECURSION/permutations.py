class Solution:
    def permutation(self,nums):
        result=[]
        def backtrack(current):
            if len(current)==len(nums):
                result.append(current[:])
                return
            for i in range(len(nums)):
                if nums[i] in current:
                    continue
                current.append(nums[i])
                backtrack(current)
                current.pop()
        backtrack([])
        return result
# Example usage:
nums=[1,2,3]
solution=Solution()
print(f"The permutations of {nums} are: {solution.permutation(nums)}")
# time complexity: O(n*n!) since there are n! permutations and each permutation takes O(n) time to construct.
# space complexity: O(n) due to the maximum depth of the recursion stack being n in the worst case when all elements are included in the current permutation.