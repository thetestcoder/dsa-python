import heapq

def sort_q(li):
    q = []
    for i in range(len(li)):
        heapq.heappush(q, li[i])
    
    sorted_q = []
    for i in range(len(q)):
        sorted_q.append(heapq.heappop(q))

    return sorted_q


li = [5, 3, 1, 4, 4, 2]

print(sort_q(li))