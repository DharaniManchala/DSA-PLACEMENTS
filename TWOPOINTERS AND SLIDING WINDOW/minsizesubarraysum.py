class Solution:

    def minSubArray(self, nums, s):

        left = 0
        currentsum = 0

        minlength = float('inf')

        for right in range(len(nums)):

            currentsum += nums[right]

            while currentsum >= s:

                minlength = min(minlength, right - left + 1)

                currentsum -= nums[left]

                left += 1

        if minlength == float('inf'):
            return 0

        return minlength