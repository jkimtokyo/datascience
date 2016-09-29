#config=utf-8

from collections import Counter
c = Counter({0, 1, 2, 3})
print(c)


for x in range(10):
    if x == 2:
        continue
    if x == 8:
        break
    print(x)