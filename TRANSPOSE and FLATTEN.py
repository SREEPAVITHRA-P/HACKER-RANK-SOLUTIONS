import numpy as np
m,n=map(int,input().split())
x=np.array([input().split() for _ in range(n)],int)
print(np.transpose(x))
print(x.flatten())

