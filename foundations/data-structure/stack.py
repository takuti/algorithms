""" stack
push and pop
"""

class Stack:
  def __init__(self, size=10):
    self.S = [0] * size
    self.top = -1

  def is_empty(self):
    if self.top == -1:
      return True
    else:
      return False

  def is_full(self):
    if self.top == len(self.S) - 1:
      return True
    else:
      return False

  def push(self, x):
    try:
      if self.is_full(): raise IndexError('the stack is full')
      self.top += 1
      self.S[self.top] = x
    except IndexError as E:
      print 'IndexError:', E

  def pop(self):
    try:
      if self.is_empty(): raise IndexError('the stack is empty')
      self.top -= 1
      return self.S[self.top+1]
    except IndexError as E:
      print 'IndexError:', E

