from collections import deque
from queue import Queue

def copyDQ(D, Q):
    while len(D) > 0:
        Q.put(D.popleft())
    return Q.queue

if __name__ == '__main__':
    D = deque([1,2,3,4,5,3,6,7,8])
    Q = Queue()
    print(copyDQ(D, Q))