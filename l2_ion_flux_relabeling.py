#!/usr/bin/env python

"""
Ion Flux Relabeling
===================

Oh no! Commander Lambda's latest experiment to improve the efficiency of her LAMBCHOP doomsday device has backfired spectacularly. She had been improving the structure of the ion flux converter tree, but something went terribly wrong and the flux chains exploded. Some of the ion flux converters survived the explosion intact, but others had their position labels blasted off. She's having her henchmen rebuild the ion flux converter tree by hand, but you think you can do it much more quickly - quickly enough, perhaps, to earn a promotion!

Flux chains require perfect binary trees, so Lambda's design arranged the ion flux converters to form one. To label them, she performed a post-order traversal of the tree of converters and labeled each converter with the order of that converter in the traversal, starting at 1. For example, a tree of 7 converters would look like the following:

   7
 3   6
1 2 4 5

Write a function answer(h, q) - where h is the height of the perfect tree of converters and q is a list of positive integers representing different flux converters - which returns a list of integers p where each element in p is the label of the converter that sits on top of the respective converter in q, or -1 if there is no such converter.  For example, answer(3, [1, 4, 7]) would return the converters above the converters at indexes 1, 4, and 7 in a perfect binary tree of height 3, which is [3, 6, -1].

The domain of the integer h is 1 <= h <= 30, where h = 1 represents a perfect binary tree containing only the root, h = 2 represents a perfect binary tree with the root and two leaf nodes, h = 3 represents a perfect binary tree with the root, two internal nodes and four leaf nodes (like the example above), and so forth.  The lists q and p contain at least one but no more than 10000 distinct integers, all of which will be between 1 and 2^h-1, inclusive.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) h = 3
    (int list) q = [7, 3, 5, 1]
Output:
    (int list) [-1, 7, 6, 3]

Inputs:
    (int) h = 5
    (int list) q = [19, 14, 28]
Output:
    (int list) [21, 15, 29] 
"""

def check_idx_value(idx, myself,parent ):
  if idx == myself:
    #print "Matched idx",idx,"value:",parent
    return True

def search_by_math(level,parent,myself,type, max_level, idx):
  if check_idx_value(idx,myself,parent):
    return parent
  distance = max_level - level
  left_child_v = myself - pow(2,distance)
  right_child_v = myself - 1
  if idx <= left_child_v:
    return search_by_math((level+1), myself, left_child_v, 'left', max_level, idx)
  else:
    return search_by_math((level+1), myself, right_child_v, 'right', max_level, idx)

def answer( h, q):
  v = pow(2,h) -1 
  return [ search_by_math(1,-1,v,'root',h, x) for x in q ]

print "(1,[1]):", answer(1,[1])
print "(30,[1]):",answer(30,[1])
print "(30,[1073741823]):",answer(30,[1073741823])
print "(3,[1,4,7]):", answer(3, [1,4,7])
print "(3,[7,3,5,1]):",answer(3, [7,3,5,1])
print "(5,[19,14,28]):",answer(5, [19,14,28])