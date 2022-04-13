from statistics import *
x, y = [list(map(int, input().split())) for i in range(2)]
mx, my = mean(x), mean(y)
print(sum([(x[i] - mx) * (y[i] - my) for i in range(len(x))]) / __import__('math').sqrt(sum([(x[i] - mx) ** 2 for i in range(len(x))]) * sum([(y[i] - my) ** 2 for i in range(len(y))])))
