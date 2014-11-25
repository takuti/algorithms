def sort(A, l, r, compare):
  def merge(m):
    n_l = m - l + 1
    n_r = r - m
    L = []
    R = []

    for i in range(n_l):
      L.append(A[l+i])
    for j in range(n_r):
      R.append(A[m+1+j])

    pos_inf = float('inf')
    neg_inf = float('-inf')
    if compare(pos_inf, neg_inf):
      L.append(pos_inf)
      R.append(pos_inf)
    else:
      L.append(neg_inf)
      R.append(neg_inf)

    i = j = 0
    for k in range(l, r+1):
      if compare(L[i], R[j]):
        A[k] = R[j]
        j += 1
      else:
        A[k] = L[i]
        i += 1

  if l < r:
    m = (l + r) / 2
    sort(A, l, m, compare)
    sort(A, m+1, r, compare)
    merge(m)

  return A
