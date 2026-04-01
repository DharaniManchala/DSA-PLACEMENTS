class Solution:
    def sortbits(self,arr):
        return sorted(arr,key=lambda x:(bin(x).count('1'),x))
# example usage:
if __name__=="__main__":
    sol=Solution()
    arr=[0,1,2,3,4,5,6,7,8]
    print(sol.sortbits(arr))  # Output: [0, 1, 2, 4, 8, 3, 5, 6, 7]

    #time complexity: O(n log n) where n is the number of elements in the array
    #space complexity: O(n) since we are using a new list to store the sorted elements

        