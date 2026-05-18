class Solution:

    def countCompleteSubarrays(self, nums):

        totaldistinct = len(set(nums))

        count = 0

        for i in range(len(nums)):

            currentset = set()

            for j in range(i, len(nums)):

                currentset.add(nums[j])

                if len(currentset) == totaldistinct:
                    count += 1

        return count


# example usage
if __name__ == "__main__":

    sol = Solution()

    nums = [1,2,3,1,2]

    print(sol.countCompleteSubarrays(nums))