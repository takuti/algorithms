# coding: utf-8

import copy

import selection
import insertion
import shell
import merge

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

if __name__ == '__main__':
  A = input_data()
  if choose_order() == 0:
    order = sort_order('ascend')
  else:
    order = sort_order('descend')

  print 'Selection: ' + str(selection.sort(copy.deepcopy(A), order))
  print 'Insertion: ' + str(insertion.sort(copy.deepcopy(A), order))
  print '    Shell: ' + str(shell.sort(copy.deepcopy(A), order))
  print '    Merge: ' + str(merge.sort(copy.deepcopy(A), 0, len(A)-1, order))
