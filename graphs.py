# CMSC 107 -- Student Solution Code
# Fall '18 Haverford College

# 
# EDIT THIS FILE
# 

from library import *

# Check whether two given nodes, n1 and n2, in g, are neighbors.
def isNeighbor(g,n1,n2):
    raise UnimplementedExecption

def getNeighbors(g, n):
    raise UnimplementedExecption

# Return the number of colors used for a given coloring
def numColors(coloring):
    raise UnimplementedExecption

# Check whether a given coloring is consistent for a graph, `g`
# Add a precondition / postcondition here if you think it's necssary
def isConsistent(g, coloring):
    raise UnimplementedExecption

#
# Predicate to test whether the coloring has the right "shape":
# everything in the coloring is a pair with its first element as a
# number, and second element is a string
# 

def looksLikeColorAssignment(colorAsn):
    return len(colorAsn) == 2 and type(colorAsn) == type(1) and type(colorAsn[2]) == type("")

def looksLikeColoring(coloring):
    forall(coloring, looksLikeColorAssignment)

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

# Is a coloring `coloring` valid for a graph `g`
@precondition(lambda g, coloring: isConsistent(g, coloring))
def isValidColoring(g, coloring):
    return UnimplementedExecption

# Check whether `coloring` is a valid k-coloring of `g`
def isValidKColoring(g, coloring, k):
    return isValidColoring(g, coloring) and numColors(coloring) <= k
