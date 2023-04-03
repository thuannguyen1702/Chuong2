a=float(input('canh 1: '))
b=float(input('canh 2: '))
c=float(input('canh 3: '))
S=float((a+b+c)/2)
#print('dien tich= ', (S*(S-a)*(S-b)*(S-c))**0.5)

import math
d=math.sqrt(S*(S-a)*(S-b)*(S-c))
print('dien tich= ', d)