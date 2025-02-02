from math import comb
import numpy as np

a=comb(40,7)
print(comb(40,7))

r=np.zeros(8)

for i in range(0,8):
    r[i]=comb(33,7-i)*comb(7,i)/a
    print(comb(33,i)*comb(7,7-i)/a)
    
result=comb(8,1)*comb(7,2)*r[1]**7*r[0]*r[3]**2
print(result)