class Solution:
    def nextsmaller(self,nums):
        stack=[]
        answer=[-1]*len(nums)
        n=len(nums)
        for i in range(n):
            while stack and nums[stack[-1]]>nums[i]:
                index=stack.pop()
                answer[index]=nums[i]
            stack.append(i)
        return answer
# Example usage:
if __name__=="__main__":
    solution=Solution()
    nums=[4,5,2,10,8]
    result=solution.nextsmaller(nums)
    print("Next smaller elements for the input array are:",result)

    #time complexity: O(n) where n is the length of the input array.
    #space complexity: O(n) for the stack and the answer array.

