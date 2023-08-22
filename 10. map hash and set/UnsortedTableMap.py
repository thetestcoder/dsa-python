from typing import Iterator
from MapBase import MapBase

class UnsortedTableMap(MapBase):
    def __init__(self) -> None:
        self._table = []

    def __getitem__(self, k):
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError("Key Error: "+ repr(k))
    
    def __setitem__(self, __key, __value):
        for item in self._table:
            if __key == item._key:
                item._value = __value
                return
        self._table.append(self._Item(__key, __value))
    
    def __delitem__(self, __key):
        for item in self._table:
            if __key == item._key:
                self._table.pop(__key)
                return
        raise KeyError("Key Error: "+ repr(__key))
    
    def __len__(self) -> int:
        return len(self._table)
    
    def __iter__(self) -> Iterator:
        for item in self._table:
            yield item._key