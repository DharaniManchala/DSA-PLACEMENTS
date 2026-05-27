class Solution:
    def combinationsum(self,combination,target):
        result=[]
        def backtrack(index,current,total):
            if total==target:
                result.append(current[:])
                return
        
            if total>target or index==len(combination):
                return
            #include
            current.append(combination[index])
            backtrack(index,current,total+combination[index])
            #exclude
            current.pop()
            backtrack(index+1,current,total)
        backtrack(0,[],0)
        return result
# Example usage:
combination=[2,3,6,7]
target=7
solution=Solution()
print(f"The combinations of {combination} that sum up to {target} are: {solution.combinationsum(combination,target)}")
# time complexity: O(2^n) in the worst case, where n is the number of elements in the combination list. This is because each element can either be included or excluded, leading to 2^n possible combinations.
# space complexity: O(n) due to the maximum depth of the recursion stack being n in