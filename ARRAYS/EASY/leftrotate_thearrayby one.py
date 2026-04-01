class Solution:
    def leftrotate(self,arr):
        n=len(arr)
        temp=[0]*n
        for i in range(1,n):
            temp[i-1]=arr[i]
        temp[n-1]=arr[0]
        for num in temp:
            print(num,end=" ")
        print()
# Example usage:
if __name__=="__main__":
    sol=Solution()
    arr=[1,2,3,4,5]
    sol.leftrotate(arr)

# Time Complexity: O(n)
# Space Complexity: O(n)

# optimal solution without using extra space
class Solution:
    def leftrotate(self,arr):
        n=len(arr)
        temp=arr[0]
        for i in range(1,n):
            arr[i-1]=arr[i]
            arr[n-1]=temp
        for num in arr:
            print(num,end=" ")
        print()
# Example usage:
if __name__=="__main__":
    sol=Solution()
    arr=[1,2,3,4,5]
    sol.leftrotate(arr)
# Time Complexity: O(n)
# Space Complexity: O(1)


        
