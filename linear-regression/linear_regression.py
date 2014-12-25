# coding: utf-8

import numpy as np

def gradient_descend(X, y, alpha=0.3):
  m = len(X)

  def f(t, x):
    return t[0] * x[0] + t[1] * x[1]

  def J(t):
    # Squared error func: (f(x)-y)^2
    s = sum([(f(t, X[i]) - y[i]) ** 2 for i in range(m)])
    return s / (2.0 * m)

  eps = 1e-7
  theta = np.zeros([len(X[0]), 1])
  while True:
    # Simultaneously update
    tmp0 = theta[0] - alpha * sum([(f(theta, X[i]) - y[i]) for i in range(m)]) / m
    tmp1 = theta[1] - alpha * sum([(f(theta, X[i]) - y[i]) * X[i][1] for i in range(m)]) / m
    if abs(J(theta) - J([tmp0, tmp1])) < eps: break
    else: theta = [tmp0, tmp1]
  return theta

def normal_equation(X, y):
  y = y[np.newaxis].T

  return np.dot(np.dot(np.linalg.inv(np.dot(X.T, X)), X.T), y)


def main():
  X = np.array([[1, -2],
                [1, -1],
                [1,  0],
                [1,  1],
                [1,  2]])
  y = np.array([[1.4],
                [1.7],
                [2.7],
                [3.4],
                [3.8]])
  print '[Gradient Descend] y = %f + %fx' % tuple(gradient_descend(X,y))
  print '[Normal Equation] y = %f + %fx' % tuple(normal_equation(X,y))


if __name__ == '__main__':
  main()
