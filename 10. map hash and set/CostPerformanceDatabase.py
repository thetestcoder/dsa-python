from SortedTableMap import SortedTableMap

class CostPerformanceDatabase:
    def __init__(self) -> None:
        self._M = SortedTableMap()

    def best(self, c):
        return self._M.find_It(c)
    
    def add(self, c, p):
        other = self._M.find_It(c)

        if other is not None and other[1] >= p:
            return
        self._M[c] = p
        other = self._M.find_ge(c)
        while other is not None and other[1] <= p:
            del self._M[other[0]]
            other = self._M.find_ge(c)