import heapq

myheap = [12, 34, 24, 55, 79, 19, 47]

heapq.heapify(myheap)
print(myheap)

print("Heap Push")
heapq.heappush(myheap, 8)
print(myheap)

print("Heap pop")
heapq.heappop(myheap)
print(myheap)