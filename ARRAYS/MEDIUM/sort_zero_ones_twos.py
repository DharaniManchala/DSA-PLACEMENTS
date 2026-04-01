class Solution:
    def sortzerosonestwos(self,nums):
        count0=0
        count1=0
        count2=0
        for num in nums:
            if num==0:
                count0+=1
            elif num==1:
                count1+=1
            else:
                count2+=1
        index=0
        for _ in range(count0):
            nums[index]=0
            index+=1
        for _ in range(count1):
            nums[index]=1
            index+=1
        for _ in range(count2):
            nums[index]=2
            index+=1
# example usage:
if __name__=="__main__":
    sol=Solution()
    nums=[2,0,2,1,1,0]
    sol.sortzerosonestwos(nums)
    print(nums)  # Output: [0, 0, 1, 1, 2, 2]

    #time complexity: O(n) where n is the number of elements in the array
    #space complexity: O(1) since we are sorting the array in place

#optimal
class Solution:
    def sortzerosonestwos(self,nums):
        low=0
        mid=0
        high=len(nums)-1
        while mid<=high:
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
# example usage:
if __name__=="__main__":
    sol=Solution()
    nums=[2,0,2,1,1,0]
    sol.sortzerosonestwos(nums)
    print(nums)  # Output: [0, 0, 1, 1, 2, 2]

    #time complexity: O(n) where n is the number of elements in the array
    #space complexity: O(1) since we are sorting the array in place