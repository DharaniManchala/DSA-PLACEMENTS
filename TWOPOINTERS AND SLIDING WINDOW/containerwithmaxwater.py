class Solution:
    def maxwater(self,height):
        left=0
        n=len(height)
        right=n-1
        maxarea=0
        while left<right:
            width=right-left
            currentarea=min(height[left],height[right])*width
            maxarea=max(maxarea,currentarea)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxarea
# Example usage:
if __name__=="__main__":
    sol=Solution()
    height=[1,8,6,2,5,4,8,3,7]
    print(sol.maxwater(height))  # Output: 49

    #time complexity: O(n)
    #space complexity: O(1)