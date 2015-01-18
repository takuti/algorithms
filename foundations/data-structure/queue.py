""" queue
enqueue and dequeue
(head and tail will circulate in queue-size)

[sample]
- - - - 1 23 14 13 2 5 8 63 - - -
        ^                   ^
      head                 tail
"""

class Queue:
  def __init__(self, size=10):
    self.Q = [0] * size
    self.head = 0
    self.tail = 0

  def __str__(self):
    return '%s head = %d, tail = %d' % (str(self.Q), self.head, self.tail)

  def enqueue(self, x):
    self.Q[self.tail] = x
    if self.tail == len(self.Q) - 1:
      self.tail = 0
    else:
      self.tail += 1

  def dequeue(self):
    x = self.Q[self.head]
    if self.head == len(self.Q) - 1:
      self.head = 1
    else:
      self.head += 1
    return x

q = Queue()
print q
