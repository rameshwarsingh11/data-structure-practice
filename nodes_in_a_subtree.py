class Node:
  def __init__(self, data):
    self.val = data
    self.children = []


def count_of_nodes(root, queries, s):
    dictionary = {}  # Provides a key value data structure

    # Traverse the tree ( treat it as a Graph ) in depth first search manner.
    def dfs(root, counters):
        if not root:
            return
        if not root.children:
            #print('Not root.children is True')
            #print(root.val)
            #print(s[root.val-1])
            dictionary[root.val] = s[root.val - 1]
            #print(dictionary)
            return
        dictionary[root.val] = s[root.val - 1]
        #print(dictionary)
        for c in root.children:
            dfs(c, counters)
            dictionary[root.val] += dictionary[c.val]
            #print('Inside for loop')
            #print(dictionary)

    dfs(root, dictionary)
    res = []
    for q in queries:
        res.append(dictionary[q[0]].count(q[1]))
        #print(res)
    return res


# Driver method
if __name__ == '__main__':

    s = "aba"
    root = Node(1)
    root.children.append(Node(2))
    root.children.append(Node(3))
    queries1 = [(1, 'a')]
    queries2 = [(2, 'b')]

    print(count_of_nodes(root, queries1, s))
    print(count_of_nodes(root, queries2, s))
