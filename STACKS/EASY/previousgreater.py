class Solution:
    def previousgreater(self,nums):
        stack=[]
        n=len(nums)
        answer=[-1]*n
        for i in range(n):
            while stack and nums[stack[-1]]<=nums[i]:
                stack.pop()
            if not stack:
                answer[i]=-1
            else:
                answer[i]=nums[stack[-1]]
            stack.append(i)
        return answer
# Example usage:
if __name__=="__main__":
    solution=Solution()
    nums=[4,5,2,10,8]
    result=solution.previousgreater(nums)
    print("Previous greater elements for the input array are:",result)

    #time complexity: O(n) where n is the length of the input array.
    #space complexity: O(n) for the stack and the answer array.