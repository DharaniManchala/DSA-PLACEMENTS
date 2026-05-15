class Solution:
    def runningsum(self,nums):
        n=len(nums)
        result=[]
        sum=0
        for i in range(n):
            sum+=nums[i]
            result.append(sum)
        return result
# example usage:
if __name__=="__main__":
    sol=Solution()
    nums=[1,2,3,4]
    result=sol.runningsum(nums)
    print(result)  # Output: [1, 3, 6, 10]

    #time complexity: O(n) where n is the length of the input array
    #space complexity: O(n) for the output array that stores the running sums
