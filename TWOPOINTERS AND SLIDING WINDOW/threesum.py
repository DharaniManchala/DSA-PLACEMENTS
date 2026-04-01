class Solution:
    def threesum(self,nums):
        nums.sort()
        result=[]
        n=len(nums)
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=n-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if total<0:
                    left+=1
                elif total>0:
                    right-=1
                else:
                    result.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
        return result
# example usage
if __name__=="__main__":
    sol=Solution()
    nums=[-1,0,1,2,-1,-4]
    result=sol.threesum(nums)
    print(result)  # Output: [[-1, -1, 2], [-1, 0, 1]]

    #time complexity: O(n^2) where n is the number of elements in the array
    #space complexity: O(n) for sorting and storing the result list