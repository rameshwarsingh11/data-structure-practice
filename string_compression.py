# Problem : Provide an algorithm to compress a string and print LetterCount pattern. Like CCAABBIIaNM should print : C2A2B2I2a1N1M1
# Note : string in python is immutable.
# Solution : Big O notation for Time & Space complexity for this algorithm is : O(n)
def compress_String(string):
  run = ""
  length = len(string)

  # Check : first edge case : if length is zero and second edge case is : if length is 1

  if length == 0:
    return ""
  if length == 1:
    return string+ "1"

  last = string[0]
  count = 1
  i = 1

  while i<length:
    if string[i] == string[i-1]: # That means if the current letter is equal to previous letter like AA then add the count + 1
      count+=1
    else:
      run = run + string[i-1]+ str(count)
      count = 1
    
    i+=1
  
  run = run + string[i-1] + str(count)
  return run

print(compress_String('AAABBBOOooNMP'))
print(compress_String('AaAAAAAAABBBBBBBSDLREOTJFNASDAAAAAAAJJJJJJJJJJJJOOOOO000OOOOOTJOERNkajdkjaurioeohrkankdfnkandkafLOPOPRJFDMCMJOEORETTtttBBBUUUuuuTTTWWWTTTT21'))