class Solution:
    def xorduplicates(self,nums):
        xor=0
        seen=set()
        for num in nums:
            if num in seen:
                xor=xor^num
            else:
                seen.add(num)
        return xor
# Example usage:
if __name__=="__main__":
    sol=Solution()
    nums=[1,2,3,2,1]
    print(sol.xorduplicates(nums))  # Output: 3

    #time complexity: O(n) where n is the number of elements in the array
    #space complexity: O(n) since we are using a set to store the seen numbers
            
        