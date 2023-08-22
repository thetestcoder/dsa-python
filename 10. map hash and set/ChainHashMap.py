from typing import Iterator
from HashMapBase import HashMapBase
from UnsortedTableMap import UnsortedTableMap

class ChainHashMap(HashMapBase):

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError("Key Error: "+ repr(k))
        return bucket[k]
    
    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()
        oldsize = len(self._table)
        self._table[j][k] = v
        if len(self._table[j]) > oldsize:
            self._n += 1
    
    def bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError("Key Error: ", repr(k))
        del bucket[k]

    def __iter__(self) -> Iterator:
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key
