########################################
# PROJECT XXX - Max Heap and Sort
# Author:
# PID:
########################################


class Heap:
    # DO NOT MODIFY THIS CLASS #
    def __init__(self, size=0):
        """
        Creates an empty hash table with a fixed capacity
        :param capacity: Initial size of the hash table.
        """
        self._array = [-1] * size
        self._capacity = len(self._array)
        self._size = size

    def __str__(self):
        """
        Prints the elements in the hash table
        :return: string
        """
        return self._array

    ###### COMPLETE THE FUNCTIONS BELOW ######

    def get_size(self):


    def has_left(self):
        pass

    def has_right(self):
        pass

    def insert(self, value):
        pass

    def remove(self, value):
        pass

    def heapify(self):
        pass

    def swap(self, i, j):
        pass

    def grow(self):
        pass

    def shrink(self):
        pass

def heapSort(unsorted):
    pass

def getStats(unsorted):
    pass
