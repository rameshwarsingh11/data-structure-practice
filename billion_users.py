# Given the grownth rates, calculate the days in which total user count will be 1B ( 1000,000,000)

def billion_users(growthrates):
  total_users = {}
  days_count = 0

  # Loop till you get total 1B users.
  while sum(total_users.values()) <= 1000000000:
      for i in range(len(growthrates)):
          if i not in total_users:
            # Add users in the array
              total_users[i] = 1
            # Multiply by growth
          total_users[i] = (total_users[i] * growthrates[i])
      days_count += 1
  return days_count


def check(expected, output):
    result = False

    if expected == output:
        result = True

    if result:
        print('Test passed.')

    else:
        print('Try again.')


# Driver method
if __name__ == '__main__':
    #print(billion_users([1.5]))
    #print(billion_users([1.1,1.2,1.3]))
    #print(billion_users([1.01,1.02]))

    test_1 = [1.1, 1.2, 1.3]
    expected_1 = 79
    output = billion_users(test_1)
    check(expected_1, output)

    test_2 = [1.5]
    expected_2 = 52
    output = billion_users(test_2)
    check(expected_2, output)
