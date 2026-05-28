class Solution:
    def mergesort(self,arr):
        if len(arr)<=1:
            return arr
        mid=len(arr)//2
        left=self.mergesort(arr[:mid])
        right=self.mergesort(arr[mid:])
        return self.merge(left,right)
    def merge(self,left,right):
        result=[]
        i=0
        j=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        while i<len(left):
            result.append(left[i])
            i+=1
        while j<len(right):
            result.append(right[j])
            j+=1
        return result
# Example usage:
arr=[38,27,43,3,9,82,10]
solution=Solution()
print(f"The sorted array is: {solution.mergesort(arr)}")
# time complexity: O(n log n) since the array is divided into two halves log n times and each merge operation takes O(n) time.
# space complexity: O(n) due to the temporary arrays used for merging.


    