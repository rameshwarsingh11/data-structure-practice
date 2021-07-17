# Find out if two rectangles overlap
def calc_overlap(coor1, dim1, coor2, dim2):

  greater = max(coor1, coor2)

  lower = min(coor1+dim1, coor2+dim2)

  if greater >= lower:
    return (None, None)  # This means there is no overlap

  # otherwise there is overlap

  overlap = lower-greater

  return (greater, overlap)


def calculate_rectangle_overlap(rect1, rect2):
  x_overlap, w_overlap = calc_overlap(rect1['x'], rect1['w'], rect2['x'], rect2['w']
                                      )
  y_overlap, h_overlap = calc_overlap(
      rect1['y'], rect2['h'], rect2['y'], rect2['h'])

  if not w_overlap or not h_overlap:
    print('No overlap.')
    return None

  print('Yes, these two rectangles overalp. Below are the overlap dimensions')
  return {'x': x_overlap, 'y': y_overlap, 'w': w_overlap, 'h': h_overlap}


print('Case 1 :::')
rect1 = {'x': 2, 'y': 4, 'w': 5, 'h': 12}
rect2 = {'x': 1, 'y': 5, 'w': 7, 'h': 14}
print(calculate_rectangle_overlap(rect1, rect2))
print('\n Case 2 :::')
rect3 = {'x': 1, 'y': 3, 'w': 3, 'h': 3}
rect4 = {'x': 2, 'y': 9, 'w': 7, 'h': 4}
print(calculate_rectangle_overlap(rect3, rect4))
print(calculate_rectangle_overlap(rect2, rect4))
