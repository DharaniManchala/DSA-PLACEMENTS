class Solution:
    def linearsearch(self,nums,num):
        for i in range(len(nums)):
            if nums[i]==num:
                return True
        return False
    def longestsequence(self,nums):
        n=len(nums) 
        if len(nums)==0:
            return 0
        longest=1
        for i in range(n):
            x=nums[i]
            count=1
            while self.linearsearch(nums,x+1):
                count+=1
                x+=1
            longest=max(longest,count)
        return longest
# example usage:
if __name__=="__main__":
    sol=Solution()
    nums=[100,4,200,1,3,2]
    result=sol.longestsequence(nums)
    print(result)  # Output: 4

    #time complexity: O(n^2) where n is the length of the input list
    #space complexity: O(1) since we are using only a constant amount of extra space

    # optimal solution
class Solution:
    def longestsequence(self,nums):
        n=len(nums)
        if n==0:
            return 0
        longest=1
        st=set(nums)
        for num in st:
            if num-1 not in st:
                count=1
                x=num
                while x+1 in st:
                    count+=1
                    x+=1
                longest=max(longest,count)
        return longest
    
# example
if __name__=="__main__":
    sol=Solution()
    nums=[100,4,200,1,3,2]
    result=sol.longestsequence(nums)
    print(result)  # Output: 4



    #time complexity: O(n) where n is the length of the input list
    #space complexity: O(n) since we are using a set to store the unique elements of the input list
    