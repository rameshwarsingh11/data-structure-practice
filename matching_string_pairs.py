def matching_pairs(source, target):
  # Checking edge case when source and target strings are same.
  if source == target:
    return len(source) - 2

  unmatched_pairs = set()
  unmatched_in_target = set()
  unmatched_in_source = set()
  count = 0
  found_perfect_swap = False
  partial_swap = False

  for i in range(len(source)):
    if source[i] == target[i]:
      count += 1
    if found_perfect_swap:
      # Skip looking for swap
      continue

    if source[i] != target[i]:
      unmatched_pairs.add((source[i], target[i]))
      unmatched_in_target.add(target[i])
      unmatched_in_source.add(source[i])

      if (target[i], source[i]) in unmatched_pairs:
        found_perfect_swap = True

      elif source[i] in unmatched_in_target or target[i] in unmatched_in_source:
        partial_swap = True

  if found_perfect_swap:
    return count + 2
  elif partial_swap:
    return count + 1


def check(expected, output):
  rightTick = '\u2713'
  wrongTick = '\u2717'

  if expected == output:
    print(rightTick, 'Test passed!')

  else:
    print(wrongTick, 'Test failed.')


if __name__ == '__main__':
  expected_1 = 4
  expected_2 = 2
  expected_3 = 3
  output_1 = matching_pairs(('abcd'), ('adcb'))
  check(expected_1, output_1)
  output_2 = matching_pairs(('aaaa'), ('aaaa'))
  check(expected_2, output_2)
  output_3 = matching_pairs(('mno'), ('nmo'))
  check(expected_3, output_3)
  print(output_1)
  print(output_2)
  print(output_3)
