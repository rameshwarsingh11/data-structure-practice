def friendSuggest(dict_friends, name_key):
    suggestedFriends = set()
    #dict_friends['Rob'] = listoffriendsofrob
    for names in dict_friends:
     for d_name in names:
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

#Rob.FriendSuggest() == [J, D, E, F]
print(friendSuggest(Rob, 'Rob'))
