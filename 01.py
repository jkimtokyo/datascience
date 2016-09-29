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

numbers = [x for x in range(5) if x %2 ==0]
print(numbers)

import random
four = [random.random() for _ in range(2)] #random.random()은 0과 1 사이 난수 생성 모듈, 여기서 레인지는 난수의 갯수가 된다.
print(four)

