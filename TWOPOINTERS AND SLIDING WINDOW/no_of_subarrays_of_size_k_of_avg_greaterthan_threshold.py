class Solution:
    def numofsubarrays(self,nums,k,threshold):
        numsum=0
        count=0
        n=len(nums)
        target=k*threshold
        for i in range(k):
            numsum=numsum+nums[i]
        if numsum>=target:
            count+=1
        for i in range(k,n):
            numsum=numsum+nums[i]
            numsum=numsum-nums[i-k]
            if numsum>=target:
                count+=1
        return count
# example usage
if __name__=="__main__":
    sol=Solution()
    nums=[2,2,2,2,5,5,5,8]
    k=3
    threshold=4
    print(sol.numofsubarrays(nums,k,threshold))

# time complexity: O(n) where n is the number of elements in the array
# space complexity: O(1) since we are using only a constant amount of extra space




