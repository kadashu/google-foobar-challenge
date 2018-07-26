#!/usr/bin/env python

'''
Prepare the Bunnies' Escape
===========================

You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny prisoners, but once they're free of the prison blocks, the bunnies are going to need to escape Lambda's space station via the escape pods as quickly as possible. Unfortunately, the halls of the space station are a maze of corridors and dead ends that will be a deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in charge of a remodeling project that will give you the opportunity to make things a little easier for the bunnies. Unfortunately (again), you can't just remove all obstacles between the bunnies and the escape pods - at most you can remove one wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing Commander Lambda's suspicions.

You have maps of parts of the space station, each starting at a prison exit and ending at the door to an escape pod. The map is represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls. The door out of the prison is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1).

Write a function answer(map) that generates the length of the shortest path from the prison door to the escape pod, where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number of nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always passable (0). The map will always be solvable, though you may or may not need to remove a wall. The height and width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
Output:
    (int) 7

Inputs:
    (int) maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
Output:
    (int) 11
'''
class node:
    def __init__(self, passable):
      self.block = passable
      self.east = None
      self.south = None
      self.west = None
      self.North = None

def build_the_route_tree( matrix, node):
    return node

search_priority = [
    [0, 1], # 0 'east'
    [1, 0], # 1 'south'
    [0,-1], # 2 'west'
    [-1,0], # 3 'north'
    ]

def next_direction( search_priority, last_direction):
    for idx, direction in  enumerate(search_priority):
        if last_direction == direction:
            return idx+1
        else:
            return 0

def next_node( maze, node, direction):
    x = node[0] + direction[0]
    if x > len(maze[0]):
        return -1
    y = node[1] + direction[1]
    if y > len(maze):
        return -1
    return maze[x,y]

def find_paths( maze, paths, direction ):
    # current node
    node = paths[-1]['path'][-1]
    x = node[0]
    y = node[1]
    v = maze[x][y]
    return []

def find_loop( path):
    return [0,0]

def answer( maze):
    paths = [{'path':[[[0,0]]],'nodes':[]}]
    find_paths( maze, paths, 'east')
    min_by_math = len(maze[0]) + len(maze) - 1
    max_steps = len(maze[0]) * len(maze)
    min = max_steps
    for p in paths:
        if p['steps'] <= min:
            min = p['steps']
            if min == min_by_math:
                return min
    return min

i1=[[0, 1, 1, 0], 
    [0, 0, 0, 1], 
    [1, 1, 0, 0], 
    [1, 1, 1, 0]]
print "maze =", i1, ":", answer(i1)

i2=[[0, 0, 0, 0, 0, 0], 
    [1, 1, 1, 1, 1, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 1, 1], 
    [0, 1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0, 0]]
print "maze =", i2, ":", answer(i2)
