#Find the list of friends which may be a good match based on common friends of a given user.
def friendSuggest(dict_friends, name_key):
    suggestedFriends = set()
    #print(B)
    #print(dict_friends)
    #dict_friends['Rob'] = list of friends of Rob
    for names in dict_friends:
     print('names:::', names)
     for d_name in names:
         for c_name in d_name:
             print('c_name:::', c_name)
            #print(d_name)
         #print('d_name:::',d_name)
             if d_name not in names:
                if d_name == name_key:
                 continue
             else:
                suggestedFriends.add(d_name)
    return suggestedFriends


Rob = ['A', 'B', 'C']
B = ['A', 'C', 'D', 'F', 'J', 'Rob']
A = ['B', 'C', 'D', 'E', 'J', 'Rob']
C = ['A', 'B', 'J', 'Rob']
D = ['B', 'A', 'F']
G = ['H', 'J']
J = ['H', 'G', 'K', 'M']

print(friendSuggest(Rob, 'Rob'))
