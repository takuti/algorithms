# coding: utf-8

import copy

def input_data():
  while True:
    try:
      a = map(int, raw_input('Input data sequence (space separated): ').split())
      return a
    except ValueError:
      print 'ValueError! Please try again!'

def choose_order():
  while True:
    try:
      order = input('[0] ascend,  [1] descend -> ')
      if order == 0 or order == 1:
        return order
      else:
        print 'Invalid input!!'
    except ValueError:
      print 'ValueError! Please try again!'

def sort_order(order='ascend'):
  if order == 'ascend':
    return lambda x, y: x > y
  elif order == 'descend':
    return lambda x, y: x < y

def selection_sort(A, compare):
  n = len(A)
  for i in range(n-1):
    selected_i = i
    for j in range(i, n):
      if compare(A[selected_i], A[j]): selected_i = j
    tmp = A[selected_i]
    A[selected_i] = A[i]
    A[i] = tmp
  return A

def insertion_sort(A, compare):
  for j in range(1, len(A)):
    key = A[j]
    i = j - 1
    while (i >= 0 and compare(A[i], key)):
      A[i+1] = A[i]
      i -= 1
    A[i+1] = key
  return A


def merge_sort(A, l, r, compare):
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
    merge_sort(A, l, m, compare)
    merge_sort(A, m+1, r, compare)
    merge(m)

  return A

if __name__ == '__main__':
  A = input_data()
  if choose_order() == 0:
    order = sort_order('ascend')
  else:
    order = sort_order('descend')

  print 'Selection: ' + str(selection_sort(copy.deepcopy(A), order))
  print 'Insertion: ' + str(insertion_sort(copy.deepcopy(A), order))
  print '    Merge: ' + str(merge_sort(copy.deepcopy(A), 0, len(A)-1, order))
