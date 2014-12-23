# coding: utf-8

import numpy as np

def gradient_descend(data, alpha=0.3):
  def f(t, x):
    return t[0] + t[1] * x

  def J(t):
    # Squared error func: (f(x)-y)^2
    s = sum([(f(t, data[i][0]) - data[i][1]) ** 2 for i in range(len(data))])
    return s / (2.0 * len(data))

  eps = 1e-7
  m = len(data)
  theta = np.zeros([m, 1])
  while True:
    # Simultaneously update
    tmp0 = theta[0] - alpha * sum([(f(theta, data[i][0]) - data[i][1]) for i in range(m)]) / m
    tmp1 = theta[1] - alpha * sum([(f(theta, data[i][0]) - data[i][1]) * data[i][0] for i in range(m)]) / m
    if abs(J(theta) - J([tmp0, tmp1])) < eps: break
    else: theta = [tmp0, tmp1]
  return theta

def normal_equation(data):
  x = data[:, 0][np.newaxis].T
  y = data[:, 1][np.newaxis].T

  print np.dot(np.dot(np.linalg.inv(np.dot(x.T, x)), x.T), y)


def main():
  # [x, y]
  data = np.array([[-2, 1.4],
                   [-1, 1.7],
                   [ 0, 2.7],
                   [ 1, 3.4],
                   [ 2, 3.8]])
  theta = gradient_descend(data)
  normal_equation(data)
  print 'y = %f + %fx' % tuple(theta)


if __name__ == '__main__':
  main()
