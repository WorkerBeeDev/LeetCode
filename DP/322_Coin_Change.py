class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        min_coins = [float('inf')] * (amount + 1)
        min_coins[0] = 0

        for i in range(amount + 1):
            for coin in coins:
                # Check that the coin is not bigger than the current amount
                if coin <= i:
                    min_coins[i] = min(min_coins[i], min_coins[i-coin] + 1)

        if min_coins[amount] == float('inf'):
            return -1
            
        return min_coins[amount]
