import numpy as np
x,y,z = map(int,input().split())
result = np.array([input().split() for _ in range(x+y)],int)
print (result)
