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

class BNode:
  def __init__(self, level):
    self.v = 0
    self.left = None
    self.right = None
    self.parent = None
    self.level = level

def check_idx(node, rets):
  if len(rets['idxs_asc']) > 0:
    idx = rets['idxs_asc'][0]
  else:
      return
  if node.v == idx:
    #print "Matched: idx", idx, "node", node.v
    if node.level == 0:
      rets['ints'][ str(idx)] = -1
      #print "keys when met root: ",rets['ints'].keys()
    else:
      if len(rets['idxs_asc']) > 0:
        rets['idxs_asc'].pop(0)
      #print "idxs_asc:",rets['idxs_asc']
      rets['ints'][ str(idx)] = node.parent


# build perfect binary tree and search idx
def search(rets, node, last_v, max_level):
  level = node.level  # AttributeError
  #print "node",node, "level", level, "last_v", last_v, "max_level", max_level
  if (max_level - level) > 1:
    if node.right == None:
      # right node not exist
      right = BNode(level+1)
      node.right = right
      right.parent = node
      if node.left == None:
        left = BNode( level+1)
        node.left = left
        left.parent = node
        search(rets, node.left,  last_v, max_level)
      elif node.left.v > 0:
        # left branch complete
        search(rets, node.right, last_v, max_level)
    elif node.right.v == 0:
      # right node exist, not complete
      search(rets, node.right, last_v, max_level )
    elif node.right.v > 0:
      # right branch complete
      if node.v == 0:
        node.v = node.right.v + 1
        #print node.v
        check_idx(node, rets)
        # free useless branch
        node.left = None
        if level == 0:
          node.right = None
        else:
          search(rets, node.parent, last_v + 1, max_level)
  elif (max_level - level) == 1:
    # bottom level
    node.v = last_v + 1
    #print node.v
    check_idx(node, rets)
    search(rets, node.parent, last_v + 1, max_level)

def answer( h, q):
  # level 0
  root = BNode(0)

  idxs_asc = sorted(q)
  ints = {}
  rets = { 'idxs': q, 'idxs_asc': idxs_asc,'ints':ints}
  search(rets, root, 0, h)
  x = []
  for idx in q:
    e = rets['ints'][str(idx)] #KeyError
    if e == -1:
      x.append( -1 )
    else:
      x.append( e.v)
  return x

print "(3,[1,4,7]):", answer(3, [1,4,7])
print "(3,[7,3,5,1]):",answer(3, [7,3,5,1])
print "(5,[19,14,28]):",answer(5, [19,14,28])
