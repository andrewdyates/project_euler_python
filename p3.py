#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright © 2011 Andrew D. Yates
# andrewyates.name@gmail.com
"""
Problem 3
http://projecteuler.net/index.php?section=problems&id=6

The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""
def sol(n):
  """Basic iterative solution."""
  summed = 0
  sq_sum = 0
  for i in range(n+1):
    summed += i
    sq_sum += i**2
  return summed**2 - sq_sum 

def comp(n):
  """Using list comprehensions"""
  sq_of_sum = sum(range(n+1))**2
  sum_of_sq = sum([x**2 for x in range(n+1)])
  return sq_of_sum - sum_of_sq

def const(n):
  """Using computational shortcut formulas"""
  sq_of_sum = ((n+1) * n/2)**2
  sum_of_sq = n * (n+1) * (2*n+1) * 1/6
  return sq_of_sum - sum_of_sq
