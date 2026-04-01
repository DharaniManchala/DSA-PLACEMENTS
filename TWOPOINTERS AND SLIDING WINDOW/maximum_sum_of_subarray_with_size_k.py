class Solution:
    def maximum_subarray(self,arr,k):
        maxsum=0
        windowsum=0
        n=len(arr)
        for i in range(n):
            windowsum+=arr[i]
        maxsum=windowsum
        for i in range(k,n):
            windowsum+=arr[i]
            windowsum-=arr[i-k]
            maxsum=max(maxsum,windowsum)
        return maxsum
# example usage
if __name__=="__main__":
    sol=Solution()
    arr=[1,2,3,4,5]
    k=2
    result=sol.maximum_subarray(arr,k)
    print(result)  # Output: 9 (subarray is [4,5])

    #time complexity: O(n) where n is the number of elements in the array
    #space complexity: O(1) since we are using only a constant amount of extra space for variables
