# coding: utf-8

def find_max_crossing_subarray(A, low, mid, high):
  """ Find max subarray crossing the middle element
  """
  left_sum, max_left = 0, 0
  s = 0
  for i in range(mid, low-1, -1):
    s += A[i]
    if s > left_sum:
      left_sum = s
      max_left = i
  right_sum, max_right = 0, 0
  s = 0
  for j in range(mid+1, high+1):
    s += A[j]
    if s > right_sum:
      right_sum = s
      max_right = j
  return (max_left, max_right, left_sum + right_sum)

def find_max_subarray(A, low, high):
  """ The maximum subarray can be separated 3-types:
  1) subarray is in the left half of A
  2) subarray is in the right half of A
  3) subarray is crossing the middle element of A
  >>> find_max_subarray([13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7], 0, 15)
  (7, 10, 43)
  """
  if low == high: return (low, high, A[low])
  mid = (low + high) / 2
  (left_low, left_high, left_sum) = find_max_subarray(A, low, mid)
  (right_low, right_high, right_sum) = find_max_subarray(A, mid+1, high)
  (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(A, low, mid, high)
  if left_sum >= right_sum and left_sum >= cross_sum:
    return (left_low, left_high, left_sum)
  elif right_sum >= cross_sum:
    return (right_low, right_high, right_sum)
  else:
    return (cross_low, cross_high, cross_sum)

def main():
  pass

if __name__ == '__main__':
  import doctest
  doctest.testmod()
  main()
