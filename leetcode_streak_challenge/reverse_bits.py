class Solution:
    def reversebits(self,n):
        result=0
        for i in range(32):
            lastbit=n&1
            n=n>>1
            result=(result<<1)|lastbit
        return result
# Example usage:
if __name__=="__main__":
    sol=Solution()
    n=43261596
    print(sol.reversebits(n))
