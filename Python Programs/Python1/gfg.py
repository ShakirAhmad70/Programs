class CoinChangeSolver:
    def __init__(self, coins):
        self.coins = coins
        self.num_coins = len(coins)
    
    def coinChangeWays(self, target_sum):
        dp = [0] * (target_sum + 1)
        dp[0] = 1
        
        for coin in self.coins:
            for i in range(coin, target_sum + 1):
                dp[i] += dp[i - coin]
        
        return dp[target_sum]

# Example usage
coins = [1, 2, 3]
coin_solver = CoinChangeSolver(coins)
sum_target = 4
result = coin_solver.coinChangeWays(sum_target)
print("Number of ways:", result)
