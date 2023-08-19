pque = []

pque.append((5, "Priority is medium"))
pque.append((1, "Priority is low"))
pque.append((10, "Priority is High"))

pque.sort(reverse=True)
print("Tasks and their priority: ")
for q in pque:
    print(q)

print("=============== popping==========")

while pque:
    print(pque.pop())