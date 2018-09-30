import unittest
from sampleData import *
from graphs import *

class TestP3(unittest.TestCase):

    # Test for warmup (showing how to use pre/postconditions)
    def test_warmup(self):
        self.assertEqual(myLen([1,2,3]), 3)

    # Write more tests here
    def test_isNeighbor(self):
        self.assertEqual(isNeighbor(graph1, 1, 2), True)
        self.assertEqual(isNeighbor(graph1, 1, 1), True)
        self.assertEqual(isNeighbor(graph2, 1, 3), False)
    
    # Write more tests here
    def test_getNeighbors(self):
        x = getNeighbors(graph1, 1)
        # Sort so that we don't penalize if you return [1,2] instead
        # of [2,1]
        x.sort()
        self.assertEqual(x, [1,2])
        x = getNeighbors(graph1, 2)
        x.sort()
        self.assertEqual(x, [1,2])
    
    # More tests here..
    def test_numColors(self):
        self.assertEqual(numColors(coloring1), 2)
        self.assertEqual(numColors(coloring2), 2)

    def test_isConsistent(self):
        self.assertEqual(isConsistent(graph1, coloring1), True)
        self.assertEqual(isConsistent(graph1, coloring2), False)

    def test_getColor(self):
        self.assertEqual(getColor(coloring1, 1), "red")
        self.assertEqual(getColor(coloring1, 2), "blue")

    def test_isValidColoring(self):
        self.assertEqual(isValidColoring(graph1, coloring1), False)
        
    def test_setEquals(self):
        self.assertEqual(setEquals([1], [1]), True)
        self.assertEqual(setEquals([], []), True)
        self.assertEqual(setEquals([2], [2]), True)
    
    def test_calculateNextSet(self):
        self.assertEqual(setEquals(calculateNextSet(graph1, [1], []), [1,2]), True)

unittest.main()
