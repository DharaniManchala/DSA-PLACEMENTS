class NumArray(object):

    def __init__(self, nums):

        self.prefix = [0] * len(nums)

        self.prefix[0] = nums[0]

        for i in range(1, len(nums)):
            self.prefix[i] = self.prefix[i-1] + nums[i]

    def sumRange(self, left, right):

        if left == 0:
            return self.prefix[right]

        return self.prefix[right] - self.prefix[left-1]
# example usage:
if __name__=="__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    numArray = NumArray(nums)
    print(numArray.sumRange(0, 2))  # Output: 1
    print(numArray.sumRange(2, 5))  # Output: -1
    print(numArray.sumRange(0, 5))  # Output: -3

    #time complexity: O(n) for the constructor to build the prefix sum array, O(1) for each sumRange query
    #space complexity: O(n) for the prefix sum array
    # def sumRange(nums, left, right):

    # prefix = [0] * len(nums)

    # prefix[0] = nums[0]

    # # Build prefix sum array
    # for i in range(1, len(nums)):
    #     prefix[i] = prefix[i-1] + nums[i]

    # # Find range sum
    # if left == 0:
    #     return prefix[right]

    # return prefix[right] - prefix[left-1]