class Solution:
    def seperatedigits(self,nums):
        result=[]
        for num in nums:
            for digit in str(num):
                result.append(int(digit))
        return result
# Example usage:
if __name__=="__main__":
    sol=Solution()
    nums=[13,25,83,77]
    print(sol.seperatedigits(nums))  # Output: [1, 3, 2, 5, 8, 3, 7, 7]

    #time complexity: O(n*m) where n is the number of elements in the input array and m is the average number of digits in each element.
    #space complexity: O(n*m) for the output array.