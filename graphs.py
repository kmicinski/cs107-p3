# CMSC 107 -- Student Solution Code
# Fall '18 Haverford College

# 
# EDIT THIS FILE
# 

# Please refer to `library.py`
from library import *

# -------------------------------------------------------------------
# Warmup: Writing decorator pre / postconditions
# -------------------------------------------------------------------

def myLen(lst):
    precondition(type(lst) == type([]))
    if (lst == []):
        precondition(0 == len(lst))
        return 0
    else:
        postcondition(1 + myLen(lst[1:]) == len(lst))
        return 1 + myLen(lst[1:])

# -------------------------------------------------------------------
# Basic Graph Operations
# -------------------------------------------------------------------

#
# Task 1 / 2
# 

# Check whether two given nodes, n1 and n2, in g, are neighbors.
def isNeighbor(g,n1,n2):
    raise UnimplementedExeception

def getNeighbors(g, n):
    raise UnimplementedExeception

# -------------------------------------------------------------------
# Graph Color Checking
# -------------------------------------------------------------------

#
# Predicate to test whether the coloring has the right "shape":
# everything in the coloring is a pair with its first element as a
# number, and second element is a string
# 

def looksLikeColorAssignment(colorAsn):
    return len(colorAsn) == 2 and type(colorAsn[0]) == type(1) and type(colorAsn[2]) == type("")

def looksLikeColoring(coloring):
    forall(coloring, looksLikeColorAssignment)

# 
# Tasks 3, 4, and 5
# 

# Task 3
# Return the number of colors used for a given coloring
# Add a precondition here if you think it's necessary
def numColors(coloring):
    raise UnimplementedExeception

# Task 4
# Check whether a given coloring is consistent for a graph, `g`
# Add a precondition / postcondition here if you think it's necssary
def isConsistent(g, coloring):
    raise UnimplementedExeception

# Task 5
# Get the color of an individual node `n`
# precondition(for all coloring, n: len(coloring) >= 1 and looksLikeColoring(coloring))
def getColor(coloring, n):
    raise UnimplementedExeception

# -------------------------------------------------------------------
# END OF P3 / BEGIN P4
# -------------------------------------------------------------------

# Task 6
# Is a coloring `coloring` valid for a graph `g`
# precondition(for all g, coloring: isConsistent(g, coloring))
def isValidColoring(g, coloring):
    raise  UnimplementedExeception

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
    return exists(lst, lambda x: x == e)

# Check that `lst` has no duplicate elements
#precondition(for all lst: type(lst) == type([]))
def noRepeats(lst): 
    if isEmpty(lst): return True
    else: return (not member(tail(lst), head(lst)) and noRepeats(tail(lst)))

# Take the union of two lists, regarded as sets
def setUnion(lst1, lst2):
    if (isEmpty(lst1)): return lst2
    elif (member(head(lst1), lst2)):
        return setUnion(tail(lst1), lst2)
    else:
        return [head(lst1)] + setUnion(tail(lst1), lst2)

# Calculate the intersection of two sets, lst1 and lst2
def setIntersection(lst1, lst2):
    if (isEmpty(lst1)): return lst2
    elif (member(head(lst1), lst2)):
        return [head(lst1)] + setUnion(tail(lst1), lst2)
    else:
        return setUnion(tail(lst1), lst2)

# Task 7
# Calculate whether or not two sets, `lst1` and `lst2`, are equal or
# not.
def setEquals(lst1, lst2):
    raise UnimplementedExeception

# -------------------------------------------------------------------
# Bipartite checking
# -------------------------------------------------------------------

# Task 8
#
# Take one "step" of the frontier. This is explained in the readme,
# but basically the idea here is to take all of the neighbors from
# every element in set A, and union them with the set B
# 
# I invite you to write a more precise precondition that states this
# mathematically
def calculateNextSet(g,A,B):
    raise UnimplementedExeception

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
