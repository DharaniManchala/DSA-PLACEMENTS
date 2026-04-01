class Solution:
    def countpairs(self,nums,k):
        nums.sort()
        left=0
        right=len(nums)-1
        count=0
        while left<right:
            if nums[left]+nums[right]<k:
                count+=(right-left)
                left+=1
            else:
                right-=1
        return count
# example usage
if __name__=="__main__":
    sol=Solution()
    nums=[1,2,3,4,5]
    k=7
    result=sol.countpairs(nums,k)
    print(result)  # Output: 6

    #time complexity: O(nlogn) due to sorting the array, where n is the number of elements in the array
    #space complexity: O(1) since we are using only a constant amount of extra space