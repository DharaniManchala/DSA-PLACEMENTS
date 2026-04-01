class Solution:
    def majorityelement(self,nums):
        result=[]
        n=len(nums)
        for num in nums:
            if num not in result:
                count=nums.count(num)
                if count>n//3:
                    result.append(num)
                if len(result)==2:
                    break
        return result
# example
if __name__=="__main__":
        sol=Solution()
        nums=[3,2,3]
        print(sol.majorityelement(nums))  # Output: [3]

    #time complexity: O(n^2) where n is the number of elements in the array
    #space complexity: O(1) since we are using only a constant amount of extra space

    # optimal
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Step 1: Find Potential Candidates
        cnt1, cnt2 = 0, 0
        el1, el2 = None, None
        
        for num in nums:
            if el1 == num:
                cnt1 += 1
            elif el2 == num:
                cnt2 += 1
            elif cnt1 == 0:
                el1 = num
                cnt1 = 1
            elif cnt2 == 0:
                el2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        # Step 2: Verify the Candidates
        cnt1, cnt2 = 0, 0
        
        for num in nums:
            if num == el1:
                cnt1 += 1
            elif num == el2:
                cnt2 += 1
        
        result = []
        mini = n // 3
        
        if cnt1 > mini:
            result.append(el1)
        if cnt2 > mini:
            result.append(el2)
        
        return result


# Example usage
if __name__ == "__main__":
    nums = [11, 33, 33, 11, 33, 11]
    sol = Solution()
    print(sol.majorityElement(nums))