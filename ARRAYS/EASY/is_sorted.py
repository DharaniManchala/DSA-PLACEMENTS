# bruteforce approach: we can use two nested loops to compare each element with every other element in the array. If we find any pair of elements where the first element is greater than the second element, then the array is not sorted and we can return False. If we finish checking all pairs without finding any such case, then the array is sorted and we can return True.
def is_sorted(arr,n):
    if n==0 or n==1:
        return True
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                return False
    return True
if __name__=="__main__":
    arr=[1,2,3,7,4,5]
    n=len(arr)
    print(is_sorted(arr,n))

    # time complexity: O(n^2) due to the nested loops
    # space complexity: O(1) since we are using only a constant amount of extra space

    # optimal approach: we can iterate through the array once and compare each element with the next element. If we find any pair of elements where the first element is greater than the second element, then the array is not sorted and we can return False. If we finish checking all pairs without finding any such case, then the array is sorted and we can return True.


# optimal approach
class Solution:
    def is_sorted(self,arr):
        n=len(arr)
        if n==0 or n==1:
            return True
        for i in range(1,n):
            if arr[i]<arr[i-1]:
                return False
        return True
if __name__ =="__main__":
    solution=Solution()
    arr=[1,2,3,4,5]
    print(solution.is_sorted(arr))
    # time complexity: O(n) where n is the number of elements in the array
    # space complexity: O(1) since we are using only a constant amount of extra
    