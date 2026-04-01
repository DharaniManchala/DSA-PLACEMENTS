class Solution:
    def kadanesalgorithm(self,nums):
        max_sum=float('-inf')
        n=len(nums)
        for i in range(n):
            sum=0
            for j in range(i,n):
                for k in range(i,j+1):
                    sum+=nums[k]
                max_sum=max(max_sum,sum)
            return max_sum
# example usage:
if __name__=="__main__":
    sol=Solution()
    nums=[-2,1,-3,4,-1,2,1,-5,4]
    result=sol.kadanesalgorithm(nums)
    print(result)  # Output: 6

    #time complexity: O(n^3) where n is the number of elements in the array
    #space complexity: O(1) since we are using only a constant amount of extra space


    # optimal solution
class Solution:
    def kandanesalgorithm(self,nums):
        max_sum=float('-inf')
        current_sum=0
        for num in nums:
            current_sum+=num
            max_sum=max(max_sum,current_sum)
            if current_sum<0:
                current_sum=0
        return max_sum
# example usage:
if __name__=="__main__":
    sol=Solution()
    nums=[-2,1,-3,4,-1,2,1,-5,4]
    result=sol.kandanesalgorithm(nums)
    print(result)  # Output: 6

    #time complexity: O(n) where n is the number of elements in the array
    #space complexity: O(1) since we are using only a constant amount of extra space