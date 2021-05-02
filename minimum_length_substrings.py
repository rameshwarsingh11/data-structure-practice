def matching_pairs(source, target):
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

print(matching_pairs(('abcd'),('adcb')))
print(matching_pairs(('dcbefebce'),('fd')))