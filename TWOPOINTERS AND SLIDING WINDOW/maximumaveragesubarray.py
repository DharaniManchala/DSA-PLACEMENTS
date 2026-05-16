# it is solveby slidingwindowconcept
class Solution:
    def maximumaveragesubarray(self,nums,k):
        sum=0
        avg=0
        result=0
        n=len(nums)
        for i in range(k):
            sum=sum+nums[i]
        avg=sum/k
        result=avg
        for i in range(k,n):
            sum=sum+nums[i]
            sum=sum-nums[i-k]
            avg=sum/k
            result=max(result,avg)
        return result
# example usage
if __name__=="__main__":
    sol=Solution()
    nums=[1,12,-5,-6,50,3]
    k=4
    print(sol.maximumaveragesubarray(nums,k))  # Output: 12.75 (subarray is [12,-5,-6,50])

    #time complexity: O(n) where n is the number of elements in the array
    #space complexity: O(1) since we are using only a constant amount of extra space for variables