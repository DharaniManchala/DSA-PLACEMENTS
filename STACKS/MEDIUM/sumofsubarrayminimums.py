class Solution:
    def previoussmaller(self,nums):
        stack=[]
        n=len(nums)
        answer=[-1]*n
        for i in range(n):
            while stack and nums[stack[-1]]>=nums[i]:
                stack.pop()
            if not stack:
                answer[i]=-1
            else:
                answer[i]=nums[stack[i]]
            stack.append(i)
        return answer
    def nextsmaller(self,nums):
        stack=[]
        n=len(nums)
        answer=[-1]*n
        for i in range(n):
            while stack and nums[stack[-1]]>nums[i]:
                index=stack.pop()
                answer[index]=nums[i]
            stack.append(i)
            return answer
        

             
             
            
            
            
            
       
    def sumofsubarray(self,nums):
        mod=10**9+7
        prev=self.previoussmaller(nums)
        next=self.nextsmaller(nums)
        total=0
        n=len(nums)
        for i in range(n):
            left=i-prev[i]
            right=next[i]-i
            contribution=nums[i]*left*right
            total=(total+contribution)%mod
        return total
# Example usage:
if __name__=="__main__":
    solution=Solution()
    nums=[3,1,2,4]
    result=solution.sumofsubarray(nums)
    print("The sum of the minimum elements of all subarrays is:",result)

    #time complexity: O(n) where n is the length of the input array.
    #space complexity: O(n) for the stack and the answer arrays.

