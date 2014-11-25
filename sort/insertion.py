""" INSERTION SORT

[algorithm]
Pick-up an element one-by-one from the head, and insert the element to appropriate position

+ Fast for almost sorted data
- Slow for non-sorted data

[order]
O(n^2)
"""

def sort(A, compare):
  """
  [arguments]
  A -- Given array
  compare -- lambda function for comparison of two values (ascend or descend)

  [return]
  Sorted array
  """
  for j in range(1, len(A)):
    key = A[j]
    i = j - 1
    while (i >= 0 and compare(A[i], key)):
      A[i+1] = A[i]
      i -= 1
    A[i+1] = key
  return A
