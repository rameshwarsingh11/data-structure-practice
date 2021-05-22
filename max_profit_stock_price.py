# Find the most beneficial transaction / max profit in the stock price list.
# Use greedy algorithm approach.

def profit(stock_prices):

  # Check edge case : If the there are less than 2 stock prices given in the stock list
  if len(stock_prices) < 2:
    raise Exception(
        'Sorry, at least two stock prices are required to compare.')

  min_stock_price = stock_prices[0]

  max_profit = 0

  for price in stock_prices:
    min_stock_price = min(min_stock_price, price)
    # print('min_stock_price',min_stock_price)
    comparison_profit = price - min_stock_price
    # print('comparison_profit',comparison_profit)
    max_profit = max(max_profit, comparison_profit)
    # print('max_profit',max_profit)
    # print('\n')
  return max_profit


def check(expected, output):
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if expected == output:
    print(rightTick, 'Test passed')

  else:
    print(wrongTick, 'Test failed.')


if __name__ == '__main__':
  expected = 15
  output = profit([45, 60, 50, 10])
  check(expected, output)
  print(output)
