# CMSC 107 -- Student Solution Code
# Fall '18 Haverford College

# 
# EDIT THIS FILE
# 

from library import *

# -------------------------------------------------------------------
# Basic Graph Operations
# -------------------------------------------------------------------

#
# Task 1 / 2
# 

# Check whether two given nodes, n1 and n2, in g, are neighbors.
def isNeighbor(g,n1,n2):
    raise UnimplementedExecption

def getNeighbors(g, n):
    raise UnimplementedExecption

# -------------------------------------------------------------------
# Graph Color Checking
# -------------------------------------------------------------------

#
# Predicate to test whether the coloring has the right "shape":
# everything in the coloring is a pair with its first element as a
# number, and second element is a string
# 

def looksLikeColorAssignment(colorAsn):
    return len(colorAsn) == 2 and type(colorAsn) == type(1) and type(colorAsn[2]) == type("")

def looksLikeColoring(coloring):
    forall(coloring, looksLikeColorAssignment)

# 
# Tasks 3, 4, and 5
# 

# Task 3
# Return the number of colors used for a given coloring
# Add a precondition here if you think it's necessary
def numColors(coloring):
    raise UnimplementedExecption

# Task 4
# Check whether a given coloring is consistent for a graph, `g`
# Add a precondition / postcondition here if you think it's necssary
def isConsistent(g, coloring):
    raise UnimplementedExecption

# You may want to think about using the following helper function in
# your implementation of `isValidColoring`

# Helper function to walk through the list of colorings at each index
# `i`. 
# 
# The idea here is that getColorHelper(coloring,n,i) looks at
# coloring[i]. coloring[i] is a pair
@precondition(lambda coloring, n, i: i < len(coloring) and looksLikeColoring(coloring))
def getColorHelper(coloring, n, i):
    if (coloring[i][0] == n):
        return coloring[i][1]
    else:
        return getColorHelper(coloring, n, i+1)

# Get the color of an individual node `n`
@precondition(lambda coloring, n: len(coloring) >= 1 and looksLikeColoring(coloring))
def getColor(coloring, n):
    return getColorHelper(coloring, n, 0)

# Task 5
# Is a coloring `coloring` valid for a graph `g`
@precondition(lambda g, coloring: isConsistent(g, coloring))
def isValidColoring(g, coloring):
    return UnimplementedExecption

# Check whether `coloring` is a valid k-coloring of `g`
def isValidKColoring(g, coloring, k):
    return isValidColoring(g, coloring) and numColors(coloring) <= k

# -------------------------------------------------------------------
# Sets
# -------------------------------------------------------------------

#
# Set operations on lists
# 

# Check whether `e` is a member of `lst`
def member(lst, e): 
    return forall(lst, lambda x: x != e)

# Check that `lst` has no duplicate elements
@precondition(lambda lst: type(lst) == type([]))
def noRepeats(lst): 
    if isEmpty(lst): return True
    else: return (not member(tail(lst), head(lst)) and noRepeats(tail(lst)))

# Take the union of two lists, regarded as sets
@precondition(lambda lst1, lst2: noRepeats(lst1) and noRepeats(lst2))
@postcondition(lambda ret: forall(lst1, lambda x: member(ret, x)) and forall(lst2, lambda x: member(ret, x)))
def setUnion(lst1, lst2):
    if (isEmpty(lst1)): return lst2
    elif (member(head(lst1), lst2)):
        return setUnion(tail(lst1), lst2)
    else:
        return [head(lst1)] + setUnion(tail(lst1), lst2)

# Calculate the intersection of two sets, lst1 and lst2
@precondition(lambda lst1, lst2: noRepeats(lst1) and noRepeats(lst2))
@postcondition(lambda ret: forall(lst1, lambda x: member(ret, x)) and forall(lst2, lambda x: member(ret, x)))
def setIntersection(lst1, lst2):
    if (isEmpty(lst1)): return lst2
    elif (member(head(lst1), lst2)):
        return [head(lst1)] + setUnion(tail(lst1), lst2)
    else:
        return setUnion(tail(lst1), lst2)

# Task 6
# Calculate whether or not two sets, `lst1` and `lst2`, are equal or
# not.
def setEquals(lst1, lst2):
    raise UnimplementedExecption

# -------------------------------------------------------------------
# Bipartite checking
# -------------------------------------------------------------------

# Task 7
#
# Take one "step" of the frontier. This is explained in the readme,
# but basically the idea here is to take all of the neighbors from
# every element in set A, and union them with the set B
# 
# I invite you to write a more precise precondition that states this
# mathematically
def calculateNextSet(g,A,B):
    raise UnimplementedExecption

# Using `calculateNextSet`, iterate the sets A and B until no more
# exploration is possible: at each step of the way, find A's neighbors
# and add them to B (using `calculateNextSet`), and then swap B with A
# to continue the exploration
def iterateFrontier(A,B):
    if (setEquals(calculateNextSet(A,B), B)):
        # Done, no work to be done
        return (A,B)
    else:
        return iterateFrontier(calculateNextSet(A,B), A)

# Pick an artbirary node in the graph to put in set `A`, and leave set
# `B` empty
def start(graph):
    return (graph[0][0], [])

# Check whether or not a graph is bipartite, using the other functions
# defined so far
def calculateBipartite(graph):
    # Calculate the final sets A and B as a pair
    answer = iterateFrontier(start(graph))
    A = answer[0]
    B = answer[1]
    return isEmpty(setIntersection(A,B))
