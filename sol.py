######################################################
#                ▄▄▄     ▄▄▄▄     ▄▄▄▄▄              #
#               ▄███    ██▀▀██   █▀▀▀▀██▄            #
#  ▄▄█████▄    █▀ ██   ██    ██       ▄██   ▄████▄   #
#  ██▄▄▄▄ ▀  ▄█▀  ██   ██ ██ ██    █████   ██▀  ▀██  #
#   ▀▀▀▀██▄  ████████  ██    ██       ▀██  ██    ██  #
#  █▄▄▄▄▄██       ██    ██▄▄██   █▄▄▄▄██▀  ▀██▄▄██▀  #
#   ▀▀▀▀▀▀        ▀▀     ▀▀▀▀     ▀▀▀▀▀      ▀▀▀▀    #
#                                                    #
######################################################
import sys, math, copy

import numpy

reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
#---------------------- USER DEFINED INPUT FUNCTIONS -----------------#
def inp():
    return(int(input()))
def mulinp():
  return([int(x) for x in input().strip().split()])
def inlt():
    return(list(map(int,input().split())))
def insertionr():
    return(input().strip())
def invr():
    return(map(int,input().split()))
#---------------------------------------------------------------------#

def sol(W, w, n):
  weights = numpy.zeros((W + 1, n + 1), dtype=int)
  for i in range(1, n + 1):
    for weight in range(1, W + 1):
      arr = [weights[weight, i - 1]]
      if w[i - 1] <= weight:
        arr.append(weights[weight - w[i - 1], i - 1] + w[i - 1])
      weights[weight, i] = max(arr)
  return weights[W, n]

  
def main():
  W, n = inlt()
  w = inlt()
  print(sol(W, w, n))


if __name__ == '__main__':
    main()
