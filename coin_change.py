# Find number of ways of change coins required for a target amount. Dynamic progrmming problem.
# Solution using bottom-up algorithm
def change_coins(n, coins):
  arr = [1] + [0]*n

  for coin in coins:
    for i in range(coin, n+1):
      arr[i] += arr[i-coin]
      # print("in loop :::", arr[i])

  # Check for edge case:
  if n == 0:
    return 0

  else:
    return arr[n]


print(change_coins(20, [5, 2, 1]))
