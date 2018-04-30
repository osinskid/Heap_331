########################################
# PROJECT XXX - Min Heap and Sort
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
        self._array = []

    def __str__(self):
        """
        Prints the elements in the hash table
        :return: string
        """
        return str(self._array)

    ###### COMPLETE THE FUNCTIONS BELOW ######

    def get_size(self):
        """
        Returns number of items currently in the hash table
        :return: int: number of items in the hash table
        """
        return len(self._array)

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def has_left(self, i):
        return self.left(i) < len(self._array)

    def has_right(self, i):
        return self.right(i) < len(self._array)

    def insert(self, value):
        self._array.append(value)
        self.upheap(len(self._array) - 1)

    def remove(self, value):
        value_index = self.find(value)
        if isinstance(value_index, int):
            self.swap(value_index, len(self._array) - 1)
            item = self._array.pop()
            self.downheap(value_index)
            return item

    def swap(self, i, j):
        self._array[i], self._array[j] = self._array[j], self._array[i]

    def upheap(self, i):
        parent = self.parent(i)
        if i > 0 and self._array[i] < self._array[parent]:
            self.swap(i, parent)
            self.upheap(parent)

    def downheap(self, i):
        if self.has_left(i):
            left = self.left(i)
            small_child = left               # although right may be smaller
            if self.has_right(i):
                right = self.right(i)
                if self._array[right] < self._array[left]:
                    small_child = right
            if self._array[small_child] < self._array[i]:
                self.swap(i, small_child)
                self.downheap(small_child)    # recur at position of small child

    def find(self, value):
        for index in range(len(self._array)):
            if self._array[index] == value:
                return index

        return False

    def remove_min(self):
        self.swap(0, len(self._array) - 1)
        item = self._array.pop()
        self.downheap(0)
        return item

def heapSort(unsorted):
    min_tree = Heap()
    sorted = []
    for element in unsorted:
        min_tree.insert(element)
    size = min_tree.get_size()
    for i in range(0, size):
        sorted.append(min_tree.remove_min())
    return sorted

def getStats(unsorted):
    sorted = heapSort(unsorted)
    dict = {}
    sum = 0
    mode = 0
    max = 0
    for element in sorted:
        if element not in dict:
            dict[element] = 0
        else:
            dict[element] += 1
        sum += element
    for val, freq in dict:
        if freq > max:
            max = freq
            mode = val
    mean = sum / len(sorted)
    median_i = len(sorted) // 2
    return [sorted[0], sorted[len(sorted)-1], mean, sorted[median_i], mode]