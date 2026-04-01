# class Solution:
#     def rotateright(self,nums,k):
#         n=len(nums)
#         k=k%n
#         temp=nums[-k:]
#         for i in range(n-k-1,-1,-1):
#             nums[i+k]=nums[i]
#         for i in range(k):
#             nums[i]=temp[i]
#     def rotateleft(self,nums,k):
#         n=len(nums)
#         k=k%n
#         temp=nums[:k]
#         for i in range(k,n):
#             nums[i-k]=nums[i]
#         for i in range(k):
#             nums[n-k+i]=temp[i]
# # Example usage:
# if __name__=="__main__":
#     sol=Solution()
#     nums=[1,2,3,4,5,6,7]
#     k=3
#     sol.rotateright(nums,k)
#     print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]
#     sol.rotateleft(nums,k)
#     print(nums)  # Output: [1, 2, 3, 4, 5, 6, 7]

#     #time complexity: O(n)
#     #space complexity: O(k)

    # optimal solution using reverse method
class Solution:
    def reverse(self,nums,start,end):
        while start<end:
            nums[start],nums[end]=nums[end],nums[start]
            start=start+1
            end=end-1
    def rotate(self,nums,k,direction):
        n=len(nums)
        if n==0 or k==0:
            return nums
        k=k%n
        if direction=="right":
            self.reverse(nums,0,n-1)
            self.reverse(nums,0,k-1)
            self.reverse(nums,k,n-1)
        elif direction=="left":
            self.reverse(nums,0,n-1)
            self.reverse(nums,0,n-k-1)
            self.reverse(nums,n-k,n-1)

# Example usage:
if __name__=="__main__":
    sol=Solution()
    nums=[1,2,3,4,5,6,7]
    k=3
    sol.rotate(nums,k,"right")
    print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]
    sol.rotate(nums,k,"left")
    print(nums)  # Output: [1, 2, 3, 4, 5, 6, 7]
    print(len(nums))

    #time complexity: O(n)
    #space complexity: O(1)
           
