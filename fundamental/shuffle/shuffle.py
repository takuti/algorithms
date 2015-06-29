import random

def random_shuffle(array):
  for tail in range(len(array)-1, 0, -1):

    # swap tail and random entry
    i = random.randint(0, tail-1)
    array[i], array[tail] = array[tail], array[i]

if __name__ == '__main__':
  array = range(10)
  print array
  random_shuffle(array)
  print array
