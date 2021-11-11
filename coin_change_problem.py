# Coin change problem :
# With recursion ( less efficient solution ) :
def rec_coin(target, coins):

  min_coins = target

  # Check base case :
  if target in coins:
    return 1

  else:
    # for every coin value that is < = the target value
    for i in [c for c in coins if c <= target]:
      num_coins = 1 + rec_coin(target-i, coins)

      # Resetting the min coins if the new num_coins is less than the min_coins
      if num_coins < min_coins:
        min_coins = num_coins

  return min_coins


# Coin change problem :
# Using Dynamic programming

def rec_coin_dynamic(target, coins, known_results):

  min_coins = target

  # Check base case :
  if target in coins:
    # Memoization. means keeping track of the already solved problems.
    known_results[target] = 1
    return 1

  elif known_results[target] > 0:
    return known_results[target]

  else:

    # For every coin vale that is <= the target values
    for i in [c for c in coins if c <= target]:
      num_coins = 1 + rec_coin_dynamic(target-i, coins, known_results)

      if num_coins < min_coins:

        min_coins = num_coins

        # Also reset the know result
        known_results[target] = min_coins

  return min_coins


target = 63
coins = [1, 5, 10, 25]
known_results = [0]*(target+1)
print(rec_coin_dynamic(target, coins, known_results))

target = 74
coins = [1, 5, 10, 25]
known_results = [0]*(target+1)
print(rec_coin_dynamic(target, coins, known_results))
