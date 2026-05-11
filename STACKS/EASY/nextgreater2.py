class Solution:
    def nextgreater2(self,nums):
        n=len(nums)
        answer=[-1]*n
        stack=[]
        for i in range(2*n):
            while stack and nums[stack[-1]]<nums[i%n]:
                index=stack.pop()
                answer[index]=nums[i%n]
            if i<n:
                stack.append(i)
        return answer
# Example usage:
if __name__=="__main__":
    sol=Solution()
    nums=[1,2,1]
    print(sol.nextgreater2(nums))  # Output: [2, -1, 2]

    #time complexity: O(n)
    #space complexity: O(n)
