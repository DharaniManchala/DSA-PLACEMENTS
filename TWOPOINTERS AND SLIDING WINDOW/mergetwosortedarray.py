class Solution:
    def mergetwosortedarray(self,nums1,nums2,m,n):
        i=m-1
        j=n-1
        k=m+n-1
        while i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i-=1
                
            else:
                nums1[k]=nums2[j]
                j-=1
            k-=1
        while j>=0:
            nums1[k]=nums2[j]
            j-=1
            k-=1
# example usage
if __name__=="__main__":
    sol=Solution()
    nums1=[1,2,3,0,0,0]
    nums2=[2,5,6]
    m=3
    n=3
    sol.mergetwosortedarray(nums1,nums2,m,n)
    print(nums1)  # Output: [1, 2, 2, 3, 5, 6]

    #time complexity: O(m+n) where m and n are the number of elements in nums1 and nums2 respectively
    #space complexity: O(1) since we are using only a constant amount of extra space

            
                