fruits = {'苹果': 2.5, '猕猴桃': 5, '西瓜': 1.9, '草莓': 10, '车厘子': 12}
import pymysql
print(pymysql.version_info)

for a in fruits.items():
    print(a)
import django
print(django.get_version())