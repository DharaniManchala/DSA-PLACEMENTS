# class Solution:
#     def subarraysumequalsk(self,nums,k):
#         count=0
#         sum=0
#         for i in range(len(nums)):
#             sum=0
#             for j in range(i,len(nums)):
#                 sum+=nums[j]
#                 if sum==k:
#                     count+=1
#         return count
# # example usage:
# if __name__=="__main__":
#     sol=Solution()
#     nums=[1,1,1]
#     k=2
#     result=sol.subarraysumequalsk(nums,k)
#     print(result)  # Output: 2

#     #time complexity: O(n^2) where n is the length of the input array
#     #space complexity: O(1) since we are using only a constant amount of extra space
#     # optimal approach
class Solution:
    def sumofsubarraysumequalsk(self,nums,k):
        count=0
        prefixsum=0
        hashmap={0:1}
        for i in range(len(nums)):
            prefixsum+=nums[i]
            if prefixsum-k in hashmap:
                count+=hashmap[prefixsum-k]
            hashmap[prefixsum]=hashmap.get(prefixsum,0)+1
        return count
# example usage:
if __name__=="__main__":
    sol=Solution()
    nums=[1,1,1]
    k=2
    result=sol.sumofsubarraysumequalsk(nums,k)
    print(result)  # Output: 2

    #time complexity: O(n) where n is the length of the input array
    #space complexity: O(n) in the worst case when all prefix sums are unique
                
        

    