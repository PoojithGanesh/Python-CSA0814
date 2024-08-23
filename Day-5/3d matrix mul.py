#Multiplication of 3 matrices
import numpy as np
a=[[1,1,1], [2,2,2], [3,3,3]]
b=[[1,1,1], [2,2,2], [3,3,3]]
c=[[1,1,1], [2,2,2], [3,3,3]]
mul=np.dot(np.dot(a,b),c)
print(mul)
