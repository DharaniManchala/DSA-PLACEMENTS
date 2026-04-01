class Solution:
    def missingnumber(self,nums):
        n=len(nums)
        total=n*(n+1)//2
        sum_of_nums=sum(nums)
        return total-sum_of_nums
# Example usage:
if __name__=="__main__":
    sol=Solution()
    nums=[0,1,2,4,5]
    print(sol.missingnumber(nums))  # Output: 3

    #time complexity: O(n)
    #space complexity: O(1)

    