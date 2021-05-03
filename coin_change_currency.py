# Find if the change coin denominations can make the target money. Return True if possible otherwise return False :


def canGetExactChange(targetMoney, denominations):

    dp = [float('inf')] * (targetMoney + 1)
    dp[0] = 0

    for coin in denominations:
        for x in range(coin, targetMoney + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return True if dp[targetMoney] != float('inf') else False


denominations = [5, 10, 25, 100, 200]
targetMoney = 94
print(canGetExactChange(targetMoney, denominations))

denominations = [4, 17, 29]
targetMoney = 75
print(canGetExactChange(targetMoney, denominations))

