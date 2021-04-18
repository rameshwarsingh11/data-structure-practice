# Find largest product from at least 3 integers list :
# Solution Time complexity : O(n), space complexity : O(1))
# Follow greedy approach to solve this problem

def highest_products(lst):
  high = max(lst[0], lst[1])
  low = min(lst[0], lst[1])

  # Keeping track of the highest & lowest 2 numbers
  high_product_2num = lst[0] * lst[1]

  low_product_2num = lst[0] * lst[1]

  # Highest product of the three numbers
  high_product_3num = lst[0]*lst[1]*lst[2]

  for num in lst[2:]:
    # Comparisions
    high_product_3num = max(high_product_3num, num *
                            high_product_2num, num*low_product_2num)

    high_product_2num = max(high_product_2num, num*high, num*low)

    low_product_2num = min(low_product_2num, num*high, num*low)

    high = max(high, num)

    low = min(low, num)

  return high_product_3num


print(highest_products([3, 4, 9, 1]))
