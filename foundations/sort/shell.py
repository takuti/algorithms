""" SHELLSORT

[algorithm]
Optimized insertion sort

1. Decide gap 'h' to get sub-data sets, and apply insertion sort for each sub-data set
2. Decrease 'h', and do above step again

For instance, gap 4 for the data [1,2,3,4,5,6,7] indicates sub-data sets [1,5], [2,6], [3,7], [4]

To decide gap sequence, using Marcin Ciura's sequence is the best way: [1,4,10,23,57,132,301,701]

[order]
In the worst case, order can be O(n^2), but average order is unknown since it depends on gap sequence.
"""

def sort(A, compare):
  """
  [arguments]
  A -- Given array
  compare -- lambda function for comparison of two values (ascend or descend)

  [return]
  Sorted array
  """
  n = len(A)
  gaps = [g for g in [701,301,132,57,23,10,4,1] if g < n]
  for gap in gaps:
    for i in range(gap, n):
      tmp = A[i]
      r = [j for j in range(i,gap-1,-gap) if compare(A[j-gap], tmp)]
      if r != []:
        for j in r:
          A[j] = A[j-gap]
        A[j-gap] = tmp
  return A
