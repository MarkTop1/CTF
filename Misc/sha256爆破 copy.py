# from codecs import Codec
# import hmac
# import imp
import hashlib
import random
from re import I

def jm_sha256_single(value):
    hsobj = hashlib.sha256()
    hsobj.update(value.encode("utf-8"))
    return hsobj.hexdigest()

while(1):
    Code=(''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a','1','2','3','4','5','6','7','8','9','0'], 6)))
    flag='TQLCTF'+Code
    print(flag)
    New=jm_sha256_single(flag)
    Key=int(New.find('5a6bb'))
    if Key == 0:
        print("请输入结果:"+flag[6:])
        break
    else:
        continue


# def jm_sha256(key, value):
#     """
#     sha256加密
#     :param key:
#     :param value: 加密字符串
#     :return: 加密结果转换为16进制字符串
#     """
#     hsobj = hashlib.sha256(key.encode("utf-8"))
#     hsobj.update(value.encode("utf-8"))
#     return hsobj.hexdigest()



    

# def hmac_sha256_single(value):
#     """
#     hmacsha256加密
#     :param value: 加密字符串
#     :return: 加密结果转换为16进制字符串
#     """
#     message = value.encode("utf-8")
#     return hmac.new(message, digestmod=hashlib.sha256).hexdigest()



# if __name__ == '__main__':
#     print("sha256加密：", jm_sha256("name", "zhangsan"))
#     print("hmacsha256加密：", hmac_sha256_single("zhangsan"))
#     print("sha256加密：", jm_sha256_single("zhangsan"))
    
