from time import time 

start_time = time()

data = range(1, 1000)

print(type(data))

end_time = time()

print("total time taken:", end_time - start_time)