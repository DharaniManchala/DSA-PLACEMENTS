class Solution:
    def twosum(self,numbers,target):
        hashmap={}
        for i in range(len(numbers)):
            complement=target-numbers[i]
            if complement in hashmap:
                return [hashmap[complement],i]
            hashmap[numbers[i]]=i
if __name__ == "__main__":
    numbers=[2,7,11,15]
    target=9
    print(Solution().twosum(numbers,target))
    # Output: [0,1]
    # time complexity is O(n) and space complexity is O(n)