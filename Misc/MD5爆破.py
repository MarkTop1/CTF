from hashlib import md5
for i in range(100000000):
    x = md5(str(i).encode()).hexdigest()
    if x.startswith('66666'):
        print(i)
        break