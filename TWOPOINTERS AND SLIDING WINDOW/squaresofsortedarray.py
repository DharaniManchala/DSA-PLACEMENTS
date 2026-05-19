def sortedsquares(nums):
    n=len(nums)
    result=[0]*n
    left=0
    right=n-1
    index=n-1
    while left<=right:
        leftsquare=nums[left]**2
        rightsquare=nums[right]**2
        if leftsquare>rightsquare:
            result[index]=leftsquare
            left+=1
        else:
            result[index]=rightsquare
            right-=1
        index-=1
    return result
# Example usage:
if __name__=="__main__":
    nums=[-4,-1,0,3,10]
    print(sortedsquares(nums))  # Output: [0, 1, 9, 16, 100]

    #time complexity: O(n)
    #space complexity: O(n)
    
