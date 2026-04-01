class Solution:
    def maxconsecutiveones(self,nums):
        count=0
        maxcount=0
        for num in nums:
            if num==1:
                count=count+1
            else:
                maxcount=max(maxcount,count)
                count=0
        maxcount=max(maxcount,count)
        return maxcount
# example usage:
if __name__=="__main__":
    sol=Solution()
    nums=[1,1,0,1,1,1]
    print(sol.maxconsecutiveones(nums))  # Output: 3

    #time complexity: O(n) where n is the number of elements in the array
    #space complexity: O(1) since we are using only a constant amount of extra space
