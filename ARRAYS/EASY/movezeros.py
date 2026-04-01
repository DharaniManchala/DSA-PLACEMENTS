class Solution:
    def movezeros(self,nums):
        n=len(nums)
        temp=[0]*n
        index=0
        for i in range(n):
            if nums[i]!=0:
                temp[index]=nums[i]
                index=index+1
        for i in range(n):
            nums[i]=temp[i]
# Example usage:
if __name__=="__main__":
    sol=Solution()
    nums=[0,1,0,3,12]
    sol.movezeros(nums)
    print(nums)  # Output: [1, 3, 12, 0, 0]

    #time complexity: O(n)
    #space complexity: O(n)
    #   optimal solution using two pointers
class Solution:
    def movezeros(self,nums):
        j=-1
        n=len(nums)
        for i in range(n):
            if nums[i]==0:
                j=i
                break
        if j==-1:
            return nums
        for i in range(j+1,n):
            if nums[i]!=0:

                nums[i],nums[j]=nums[j],nums[i]
                j=j+1
# Example usage:
if __name__=="__main__":
    sol=Solution()
    nums=[0,1,0,3,12]
    sol.movezeros(nums)
    print(nums)  # Output: [1, 3, 12, 0, 0]

    #time complexity: O(n)
    #space complexity: O(1)



    





