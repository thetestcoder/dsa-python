from MapBase import MapBase

class SortedTableMap(MapBase):
    def _find_index(self, k, low, high):
        if high < low:
            return high + 1
        else:
            mid = (high + low) // 2
            if k == self._table[mid]._key:
                return mid
            elif k < self._table[mid]._key:
                return self._find_index(k, low, mid-1)
            else:
                return self._find_index(k, mid+1, high)
            
    
    def __init__(self):
        self._table = []

    
    def __len__(self) -> int:
        return len(self._table)
    
    def __getitem__(self, __key):
        j = self._find_index(__key, 0, len(self._table)-1)
        if j == len(self._table) or self._table[j]._key != __key:
            raise KeyError("Key error: "+ repr(__key))
        return self._table[j]._value


    def __setitem__(self, key, v):
        j = self._find_index(key, 0, len(self._table) - 1)
        if j < len(self._table) or self._table[j]._key == key:
            self._table[j]._value = v
        else:
            self._table.insert(j, self._Item(key, v))

    def __delitem__(self, __key):
        j = self._find_index(__key, 0, len(self._table)-1)
        if j == len(self._table) or self._table[j]._key != __key:
            raise KeyError("Key error: "+ repr(__key))
        self._table.pop(j)

    def __iter__(self):
        for item in self._table:
            yield item._key

    def __reversed__(self):
        for item in reversed(self._table):
            yield item._key

    def find_min(self):
        if len(self._table) > 0:
            return (self._table[0]._key, self._table[0]._value)
        else:
            return None

    def find_max(self):
        if len(self._table) > 0:
            return (self._table[-1]._key, self._table[-1]._value)
        else:
            return None
