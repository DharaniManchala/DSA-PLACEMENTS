# 📄 Problem Statement

# Given a non-empty array of integers:

# Every element appears twice
# Except for one element, which appears only once

# 👉 Find that single element.
class Solution:
    def numberappearonceandothertwice(self,nums):
        n=len(nums)
        for i in range(n):
            num=nums[i]
            count=0
            for j in range(n):
                if nums[j]==num:
                    count=count+1
            if count==1:
                return num
        return -1
# Example usage:
if __name__=="__main__":
    sol=Solution()
    nums=[2,2,1]
    print(sol.numberappearonceandothertwice(nums))  # Output: 1

    #time complexity: O(n^2) where n is the number of elements in the array
    #space complexity: O(1) since we are using only a constant amount of extra space

    # optimal solution using XOR operator
class Solution:
    def numberappearonce(self,nums):
        xor=0
        for num in nums:
            xor=xor^num
        return xor
# Example usage:
if __name__=="__main__":
    sol=Solution()
    nums=[2,2,1]
    print(sol.numberappearonce(nums))  # Output: 1

    #time complexity: O(n) where n is the number of elements in the array
    #space complexity: O(1) since we are using only a constant amount of extra space

            

