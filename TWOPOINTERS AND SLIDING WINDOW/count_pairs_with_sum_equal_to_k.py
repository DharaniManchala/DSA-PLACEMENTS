class Solution:
    def count_pairs_with_sum_equal_to_k(self,arr,k):
        freq={}
        count=0
        for num in arr:
            need=k-num
            if need in freq:
                count+=freq[need]
            freq[num]=freq.get(num,0)+1
        return count
# example usage
if __name__=="__main__":
    sol=Solution()
    arr=[1,2,3,4,5]
    k=5
    result=sol.count_pairs_with_sum_equal_to_k(arr,k)
    print(result)  # Output: 2 (pairs are (1,4) and (2,3))

    #time complexity: O(n) where n is the number of elements in the array
    #space complexity: O(n) in the worst case if all elements are unique and stored in the frequency dictionary


