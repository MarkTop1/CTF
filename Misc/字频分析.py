# 提取前16位字符

from collections import Counter
import string

c = open('H:/Python3.0Work/test.txt').read()
c = Counter(c)
print(c.most_common())

for i in range(16):   
    print(c.most_common()[i][0], end = '')