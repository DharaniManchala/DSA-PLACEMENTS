# class Solution:
#     def reversearray(self,arr):
#         n=len(arr)
        
#         for i in range(n//2):
#             temp=arr[i]
#             arr[i]=arr[n-i-1]
#             arr[n-i-1]=temp
#         return arr
# # example usage
# solution = Solution()
# arr = [1, 2, 3, 4, 5]
# reversed_arr = solution.reversearray(arr)
# print(reversed_arr)  # Output: [5, 4, 3, 2, 1]
# # Time complexity: O(n)
# # Space complexity: O(1)

# two pointer style
class Solution:
    def reversearray(self,arr):
        left,right=0,len(arr)-1
        while left<right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
        return arr
# example usage
solution = Solution()
arr = [1, 2, 3, 4, 5]
reversed_arr = solution.reversearray(arr)
print(reversed_arr)  # Output: [5, 4, 3,

# Time complexity: O(n)
# Space complexity: O(1)
