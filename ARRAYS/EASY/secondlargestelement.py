# bruteforce
def get_elements(arr,n):
    if n==0 or n==1:
        print(-1,-1)
        return 
    arr.sort()
    smallest=arr[0]
    largest=arr[-1]
    secondlarge=arr[n-2]
    print("smallestis",smallest)
    print("largest is",largest)
    print("second largest is",secondlarge)
if __name__=="__main__":
    arr=[1,2,3,4,5]
    n=len(arr)
    get_elements(arr,n)

    # time complexity: O(nlogn) due to sorting the array
    # space complexity: O(1) since we are using only a constant amount of extra space

   

   
# optimal
class Solution:
    def secondlargestelement(self,nums):
        if len(nums)<2:
            return -1
        largest=secondlargest=float('-inf')
        for num in nums:
            if num>largest:
                secondlargest=largest
                largest=num
            elif largest>num>secondlargest:
                secondlargest=num
        return secondlargest
# Example usage:
solution=Solution()
nums=[3,1,4,1,5,9]
print(solution.secondlargestelement(nums))
# time complexity: O(n) where n is the number of elements in the array
# space complexity: O(1) since we are using only a constant amount of extra space
                



        