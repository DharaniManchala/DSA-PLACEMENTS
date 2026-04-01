class Solution:
    def avgofsubarrays(self,arr,k):
        result=[]
        winsum=0
        winstart=0
        n=len(arr)
        for winend in range(n):
            winsum+=arr[winend]
            if winend>=k-1:
                result.append(winsum/float(k))
                winsum-=arr[winstart]
                winstart+=1
        return result
# example usage
if __name__=="__main__":
    sol=Solution()
    arr=[1,2,3,4,5]
    k=2
    result=sol.avgofsubarrays(arr,k)
    print(result)  # Output: [1.5, 2.5, 3.5, 4.5]

    #time complexity: O(n) where n is the number of elements in the array
    #space complexity: O(n-k+1) for storing the result list which contains the averages of the subarrays of size k