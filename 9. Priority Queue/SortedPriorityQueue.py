from PriorityQueueBase import PriorityQueueBase
from EmptyException import EmptyException
from PositionalList import PositionalList

class SortedPriorityQueue(PriorityQueueBase):
    
    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)
    
    def add(self, key, value):
        newest =  self._Item(key, value)
        walk = self._data.last()
        if walk is None:
            self._data.add_first(walk)
        else:
            self._data.add_after(walk, newest)
    

    
    def min(self):
        if self.is_empty(): raise EmptyException("Priority Queue is Empty")
        item = self._data.first()
        return (item._key, item._value)
    
    def remove_min(self):
        if self.is_empty(): raise EmptyException("Priority Queue is Empty")
        item = self._data.delete(self._data.first())
        return (item._key, item._value)
    
    