import unittest
from insertionsort import insertion_sort
from mergeSort import merge_sort

class SortTestCase(unittest.TestCase):
    def test_insertion_sort(self):
        A = [2,3,1,5,6,4]
        B = [1,2,3,4,5,6]
        C = [6,5,4,3,2,1]

        sortList = [1,2,3,4,5,6]
        insertion_sort(A)
        insertion_sort(B)
        insertion_sort(C)
        self.assertListEqual(A, sortList)
        self.assertListEqual(B, sortList)
        self.assertListEqual(C, sortList)
        
    def test_merge_sort(self):
        A = [2,3,1,5,6,4]
        B = [1,2,3,4,5,6]
        C = [6,5,4,3,2,1]

        sortList = [1,2,3,4,5,6]
        merge_sort(A, 0, 5)
        merge_sort(B, 0, 5)
        merge_sort(C, 0, 5)

        self.assertListEqual(A, sortList)
        self.assertListEqual(B, sortList)
        self.assertListEqual(C, sortList)

