hz1 = [1209,1336,1477,1633]
hz2 = [697,770,852,941]
table = ['1','2','3','A','4','5','6','B','7','8','9','C','*','0','#','D']

s = '1336-697 1477-697 1477-697 1336-770 1209-852 1477-697 1336-770 1209-852 1336-941 1209-770 1209-852 1209-697 1209-697 1336-697 1336-941 1336-941 1477-770 1209-697 1477-770 1209-770 1477-697 1477-770 1209-770 1209-852 1336-852 1336-697 1336-852 1477-770 1477-852 1209-852 1209-697 1209-697 1336-941 1477-852 1477-770 1209-852 1209-852 1209-852 1477-697 1477-770 1336-852 1477-852 1336-852 1336-770 1336-852 1209-852 1336-941 1336-697 1336-697 1336-852 1477-697 1336-697 1336-770 1477-697 1209-852 1209-697 1477-697 1209-770 1477-697 1209-852 1336-852 1209-852 1209-770 1477-697 1336-852 1209-697 1477-697 1336-697 1477-852 1209-697 1209-770 1336-697 1336-697 1477-852 1209-697 1477-770 1477-770 1336-852 1336-852 1209-770 1477-697 1209-770 1209-770 1336-697 1336-852 1336-941 1336-941 1336-770 1336-852 1477-770 1336-697 1477-770 1477-697 1336-697 1336-852 1209-770 1336-941 1336-770 1336-852 1336-697 1209-770 1336-770 1336-852 1336-697 1477-852 1477-852 1336-852 1477-697 1209-770 1477-852 1336-852'
s = s.split(' ')
flag = ''
for i in s:
    _hz1 = int(i[:4])
    _hz2 = int(i[-3:])
    for k in range(len(hz1)):
        if(hz1[k] == _hz1):
            for j in range(len(hz2)):
                if(hz2[j] == _hz2):
                    flag += table[j*4+k]
                    break
print(flag)
import libnum
print(libnum.n2s(int(flag)))
