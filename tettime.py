import time
import numpy as np
l = 10000000
start = time.time()

a = np.arange(l)
b = np.arange(l)
c = a * b

t = time.time() - start
print( " Tempo: %s" % t)
