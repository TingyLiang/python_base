import hashlib

md5 = hashlib.md5()

# 无论使用何种编码方式，统一hash算法获得的hash值都是相同的
md5.update("encryption by md5".encode("utf-8"))
print(md5.hexdigest())
md5 = hashlib.md5()
md5.update("encryption by md5".encode("GBK"))
print(md5.hexdigest())

sh1 = hashlib.sha1()
sh1.update("encryption by md5".encode("utf-8"))
print(sh1.hexdigest())

# hash 加盐

md5 = hashlib.md5()
md5.update(("123456" + "the salt").encode("utf-8"))
print(md5.hexdigest())
# 在存储用户数据的时候，可以使用用户名作为盐，这样使得使用相同密码的用户，可以有不同的hash口令值
