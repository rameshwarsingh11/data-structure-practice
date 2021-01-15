# Coin Change problem / Change taking / knapsack type problem
# Problem : Given a target amount n with distinct coins. Find out the minimun/fewest coins needed to make the change amount.
# For instance n = 10 and distinct list of coins = [1,5,10] then the solution should provide 4 ways to get 10 :
#  1. 10 ones = 1+1+1+1+1+1+1+1+1+1+1
#  2. 1 five and 5 ones = 5 + 1+1+1+1+1
#  3. 2 Fives = 5+5
#  4. 1 ten = 10

# Solution : Using recursion ( Not efficient solution)

def recursion_coin(target_coin,coins_list):
  # Setting default to min coins required:
  min_coins = target_coin

  # Check base case to see if target_coin is in coins_list
  if target_coin in coins_list:
    return 1

  else:
    # For every coin value that is <= target value (n)
    for i in [c for c in coins_list if c<= target_coin]:
      # Add a coin count and add to the recursive call.
      num_of_coins = 1 + recursion_coin(target_coin-i, coins_list)

      # Resetting the minimum coins here if the new num of coins is less then the minimum number of coins
      if num_of_coins < min_coins:
        min_coins = num_of_coins

  return min_coins

print(recursion_coin(20,[1,5,10]))
# print(recursion_coin(78,[1,5,10,25]))
# Above is time consuming solution for more complex problems like when target_coin = 78.

# Solution 2 : Using Dynamic Programming ( Memoization) [ Efficient Solution]
# This approves saves the intermediary results in a cache for better performance and avoid recalculations.
# This approach is efficient in Time but not much efficient in space as it will use more memory to store cached results.
# This is space trades off but better than plain recursion approach.

def rec_dynamic_coin(target_coin, coins_list, known_results):
 # Setting default to min coins required:
  min_coins = target_coin

  # Check base case
  if target_coin in coins_list:
    known_results[target_coin] = 1
    return 1
  

  # Return a known result if it is greater than 1
  elif known_results[target_coin] >0:
    return known_results[target_coin]

  else:
    # For every coin value that is less than or equal than the target coin
    for i in [ c for c in coins_list if c<=target_coin ]:
      # Make a recursion call
      num_coins = 1 + rec_dynamic_coin(target_coin - i,coins_list, known_results)

      # Ressting the minimum coins
      if num_coins< min_coins:
        min_coins = num_coins

        # Also reset that known result like clear the cache !
        known_results[target_coin] = min_coins

      
  return min_coins

target_coin = 74
coins_list = [1,5,10,25]
known_results = [0]*(target_coin+1)

print(rec_dynamic_coin(target_coin,coins_list,known_results))