class Solution:
    def twosum2(self,numbers,target):
        left=0
        right=len(numbers)-1
        currentsum=0
        while left<right:
            currentsum=numbers[left]+numbers[right]
            if currentsum==target:
                return [left+1,right+1]
            elif currentsum<target:
                left+=1
            else:
                right-=1
if __name__ == "__main__":
    numbers=[2,7,11,15]
    target=9
    print(Solution().twosum2(numbers,target))
    # Output: [1,2]
    # time complexity is O(n) and space complexity is O(1)
