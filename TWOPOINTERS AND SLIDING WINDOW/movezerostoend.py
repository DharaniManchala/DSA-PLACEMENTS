class Solution:
    def movezerostoend(self,arr):
        n=len(arr)
        slow=0
        for fast in range(1,len(nums)):
            if arr[fast]!=0:
                arr[slow],arr[fast]=arr[fast],arr[slow]
                slow+=1
        return arr

# example usage
if __name__=="__main__":
    sol=Solution()
    arr=[0,1,0,3,12]
    result=sol.movezerostoend(arr)
    print(result)  # Output: [1, 3, 12, 0, 0]

    #time complexity: O(n) where n is the number of elements in the array
    #space complexity: O(1) since we are using only a constant amount of extra space