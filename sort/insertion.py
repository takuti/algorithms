def sort(A, compare):
  for j in range(1, len(A)):
    key = A[j]
    i = j - 1
    while (i >= 0 and compare(A[i], key)):
      A[i+1] = A[i]
      i -= 1
    A[i+1] = key
  return A
