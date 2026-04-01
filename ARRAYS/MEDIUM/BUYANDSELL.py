class Solution:
    def buyandsell(self,prices):
        minprice=float('inf')
        maxprofit=0
        n=len(prices)
        for i in range(1,n):
            for j in range(i+1,n):
                maxprofit=max(maxprofit,prices[j]-prices[i])
        return maxprofit
# example usage:
if __name__=="__main__":
    sol=Solution()
    prices=[7,1,5,3,6,4]
    result=sol.buyandsell(prices)
    print(result)  # Output: 5

    #time complexity: O(n^2) where n is the length of the input list
    #space complexity: O(1) since we are using only a constant amount of extra space

    # optimmal solution
class Solution:
    def buyandsell(self,prices):
        minprice=float('inf')
        maxprofit=0
        for price in prices:
            if price<minprice:
                minprice=price
            else:
                maxprofit=max(maxprofit,price-minprice)
        return maxprofit
# example usage:
if __name__=="__main__":
    sol=Solution()
    prices=[7,1,5,3,6,4]
    result=sol.buyandsell(prices)
    print(result)  # Output: 5

    #time complexity: O(n) where n is the length of the input list
    #space complexity: O(1) since we are using only a constant amount of extra space
