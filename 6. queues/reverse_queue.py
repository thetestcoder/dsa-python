from queue import Queue

def reverseQueue(q):
    if not q.empty():
        front= q.get()
        reverseQueue(q)
        q.put(front)
    return q
    

if __name__ == '__main__':
    q = Queue()
    for i in range(5):
        q.put(i)
    print(reverseQueue(q).queue)