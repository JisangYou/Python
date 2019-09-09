import time
import numpy as np

x = np.random.random(100000000)

# 14.688855171203613초

start = time.time()
sum(x) / len(x)
print(time.time() - start)

# 0.1410841941833496초

start = time.time()
np.mean(x)
print(time.time() - start)
