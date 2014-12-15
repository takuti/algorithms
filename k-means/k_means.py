# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.vq import vq, kmeans, kmeans2, whiten

def read_iris():
  """ read iris dataset as a list of values
  """
  lines = map(lambda l: l.rstrip('\n'), open('../@data/iris.data').readlines())
  X = []
  label = []
  for l in lines:
    l = l.split(',')
    X.append(map(float, l[:4]))
    label.append(l[4])
  return np.array(X), np.array(label)

def main():
  X, label = read_iris()
  whitened = whiten(X) # normalize
  method = input('[0] minimize distortion k-means, [1] random initialize k-means > ')
  if method == 0:
    centroid, distortion = kmeans(whitened, k_or_guess=3)
    alloc = vq(whitened, centroid)[0]
  else:
    centroid, alloc = kmeans2(whitened, k=3)
  c = [[] for i in range(3)] # k = 3
  for i in range(len(X)):
    c[alloc[i]].append(label[i])
  print c[0]
  print c[1]
  print c[2]

if __name__ == '__main__':
  main()
