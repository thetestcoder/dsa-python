from MapBase import MapBase
from random import randrange


class HashMapBase(MapBase):
    def __init__(self, cap=11, p=109345121):
        self._table = cap * [None]
        self._n = 0
        self._prime = p
        self._scale = 1 + randrange(p-1)
        self._shift = randrange(p)

    def _hash_function(self, k):
        return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)
    
    def __len__(self) -> int:
        return self._n
    
    def __getitem__(self, __key):
        j = self._hash_function(__key)
        return self._bucket_getitem(j, __key)
    
    def __setitem__(self, __key, __value):
        j = self._hash_function(__key)
        self._bucket_setitem(j, __key, __value)
        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table) - 1)

    def __delitem__(self, __key) -> None:
        j = self._hash_function(__key)
        self._bucket_delitem(j, __key)
        self._n -= 1
    
    def _resize(self, c):
        old = list(self.items())
        self._table = c * [None]
        self._n = 0
        for (k, v) in old:
            self[k] = v


