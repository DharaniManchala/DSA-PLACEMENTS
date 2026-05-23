class Solution:
    def smallestletter(self,letters,target):
        left=0
        right=len(letters)-1
        while left<=right:
            mid=(left+right)//2
            if letters[mid]<=target:
                left=mid+1
            else:
                right-=1
        return letters[left%len(letters)]
# Example usage:
if __name__=="__main__":
    sol=Solution()
    letters=["c","f","j"]
    target="a"
    result=sol.smallestletter(letters,target)
    print("Smallest letter greater than target:", result)

    # time complexity: O(log n) where n is the number of elements in the array
    # space complexity: O(1) since we are using only a constant amount of extra space