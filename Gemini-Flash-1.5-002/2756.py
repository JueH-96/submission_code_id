class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        if len(prices) < 2:
            return money
        
        cost = prices[0] + prices[1]
        if cost <= money:
            return money - cost
        else:
            return money