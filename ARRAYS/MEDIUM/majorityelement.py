# bruteforceapproach
class Solution:
    def majorityelement(self,nums):
        n=len(nums)
        for i in range(n):
            num=nums[i]
            count=0
            for j in range(n):
                if nums[j]==num:
                    count=count+1
            if count>n//2:
                return num
        return -1
    # example
if __name__=="__main__":
        sol=Solution()
        nums=[2,2,1,1,1,2,2]
        print(sol.majorityelement(nums))  # Output: 2
    #time complexity: O(n^2) where n is the number of elements in the array
    #space complexity: O(1) since we are using only a constant amount of extra space

# optimal approach
# moores  voting algorithm
class Solution:
    def majorityelement(self,nums):
        n=len(nums)
        count=0
        element=0
        for num in nums:
            if count==0:
                element=num
                count=1
            elif num==element:
                count+=1
            else:
                count-=1
        cnt1=nums.count(element)
        if cnt1>(n//2):
            return element
        return -1
# example
if __name__=="__main__":
        sol=Solution()
        nums=[2,2,1,1,1,2,2]
        print(sol.majorityelement(nums))  # Output: 2
    #time complexity: O(n) where n is the number of elements in the array
    #space complexity: O(1) since we are using only a constant amount of extra space





