# Find possible permutations of a string using recursion.
def find_permutations(string):
  
  output = []

  # Check base case :
  if len(string) ==1:
    output = [string]
  
  else:
    # Loop for every letter in the string use enumerate method
    for i,letter in enumerate(string):
      # Now for every permutation getting from above steps, call find_permutations method recursively.
      for permutation in find_permutations(string[:i] + string[i+1:]): #string[:1] means go till everything upto index i and string[i+1:0] means go through all the way till the end from index i+1
        # For better understanding of the logic, print the middle outputs.
        print('Current Letter', letter)
        print('Current permutation :',permutation)
        
        # Add to my output list
        output = output + [letter + permutation] 

  return output

print(find_permutations('TBD'))