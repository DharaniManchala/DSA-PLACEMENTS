class Solution:
    def trappingrainwater(self,height):
        left=0
        n=len(height)
        right=n-1
        leftmax=0
        rightmax=0
        water=0
        while left<=right:
            if height[left]<=height[right]:
                if height[left]>=leftmax:
                    leftmax=height[left]
                else:
                    water+=leftmax-height[left]
                left+=1
            else:
                if height[right]>=rightmax:
                    rightmax=height[right]
                else:
                    water+=rightmax-height[right]
                right-=1
        return water
# Example usage:
if __name__=="__main__":
    sol=Solution()
    height=[0,1,0,2,1,0,1,3,2,1,2,1]
    print(sol.trappingrainwater(height))  # Output: 6

    #time complexity: O(n) where n is the number of elements in the height array
    #space complexity: O(1) since we are using only a constant amount of extra space for the pointers and variables.

        