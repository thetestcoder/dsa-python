from TreeMap import TreeMap

class SplayTreeMap(TreeMap):
    def _splay(self, p):
        while p != self.root():
            parent = self.parent(p)
            grand = self.parent(parent)
            if grand is None:
                #zig case
                self._rotate(p)
            elif (parent == self.left(grand) == (p == self.left(parent))):
                # zig-zig case
                self._rotate(parent)
                self._rotate(p)
            else:
                #zig-zag case
                self._rotate(p)
                self._rotate(p)

    
    def _rebalance_insert(self, p):
        self._splay(p)

    def _rebalance_delete(self, p):
        self._splay(p)

    def _rebalance_access(self, p):
        self._splay(p)