# Find the maximum possible value from an unsorted list of numbers.
# Use counting sort algorithm

def max_value(unsorted_prices, max_price):
  prices_to_counts = [0]*(max_price+1)

  for price in unsorted_prices:
    prices_to_counts[price] += 1

  sorted_prices = []

  for price, count in enumerate(prices_to_counts):
    for time in range(count):
      sorted_prices.append(price)

  return sorted_prices[-1::][0]

print(max_value([45, 67, 34, 21, 78, 90, 5], 90))
