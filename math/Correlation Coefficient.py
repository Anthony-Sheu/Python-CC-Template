from statistics import *
from math import *
x, y = gi(), gi()
mx, my = mean(x), mean(y)
print(sum([(x[i]-mx)*(y[i]-my) for i in range(len(x)])/sqrt(sum([(x[i]-mx)**2 for i in range(len(x)]) * sum([(y[i]-my)**2 for i in range(len(y)])))
