def sort(A, compare):
  n = len(A)
  for i in range(n-1):
    selected_i = i
    for j in range(i, n):
      if compare(A[selected_i], A[j]): selected_i = j
    tmp = A[selected_i]
    A[selected_i] = A[i]
    A[i] = tmp
  return A
