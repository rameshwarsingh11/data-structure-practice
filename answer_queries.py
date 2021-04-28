"""
Imagine a length-N array of booleans, initially all false. Over time, some values are set to true, and at various points in time you would like to find the location of the nearest true to the right of given indices.
You will receive Q queries, each of which has a type and a value. SET queries have type = 1 and GET queries have type = 2.
When you receive a SET query, the value of the query denotes an index in the array that is set to true. Note that these indices start at 1. When you receive a GET query, you must return the smallest index that contains a true value that is greater than or equal to the given index, or -1 if no such index exists.
Signature
int[] answerQueries(ArrayList queries, int N)
Input
A list of Q queries, formatted as [type, index] where type is either 1 or 2, and index is < N
1 <= N <= 1,000,000,000
1 <= Q <= 500,000
Output
Return an array containing the results of all GET queries. The result of queries[i] is the smallest index that contains a true value that is greater than or equal to i, or -1 if no index satisfies those conditions.
Example
N = 5
Q = 5
queries = [[2, 3], [1, 2], [2, 1], [2, 3], [2, 2]]
output = [-1, 2, -1, 2]
"""


def answerQueries(queries, N):

  default_value = -1
  answer = []
  pos = 0

  # By default all values in the array is False
  array = [False for i in range(N)]

  for query in queries:
    #print('Current query :::', query)
    #print('Current array :::', array)
    #print('Current answer array :::', answer)

    # Set query case :
    if query[0] == 1:
        # Get the value of the query as index position to be set as True in the answer array.
        array[query[1] - 1] = True

    # Get query case :
    elif query[0] == 2:
        searching = True
        pos = query[1] - 1  # indices are 1 based.

        # Search along the rest of the array to find the smallest index that contains a True value that is greater than or equal to the given index
        while searching & (pos < len(array)):
            # Only append if there is any True value in the array.
            if array[pos]:
                # If yes, append the index position in the answer array.
                answer.append(pos + 1)
                searching = False
            pos += 1  # Keep going.

        # If there is no true value present in the array then append the default value of -1 in the answer array.
        if searching:
            answer.append(default_value)

    #print('"""""""""""""""""""""""""""')
    #print('Updated array  :::', array)
    #print('Updated answer array :::', answer)
    #print('"""""""""""""""""""""""""""')

  return answer


def check(expected, output):
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if expected == output:
        print(rightTick, 'Test passed.')

    else:
        print(wrongTick, 'Test failed')


# Driver method :
if __name__ == '__main__':
    N = 5
    # 2 denotes GET query and 1 denotes SET query.
    queries = [[2, 3], [1, 2], [2, 1], [2, 3], [2, 2]]
    output = answerQueries(queries, N)
    expected = [-1, 2, -1, 2]
    check(expected, output)
    print('Final answer array ::: ', answerQueries(queries, N))
