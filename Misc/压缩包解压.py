import zipfile

path = 'F:/Download/' # 工作文件夹
name = '0573' # 起始压缩包名
while True:
    zipname = path + name + '.zip' # 生成完整的待解压压缩包名
    print(name)
    ts1 = zipfile.ZipFile(zipname)
    password = bytes(name, 'utf-8') # 解压密码就是文件名
    ts1.extractall(path, pwd = password) # 解压得到下一个压缩包
    name = ts1.namelist()[0].split('.')[0] # 读取压缩包内的下一个压缩包的文件名，以供下一个循环使用