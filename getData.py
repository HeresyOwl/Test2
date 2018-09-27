#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import pymysql
from datetime import datetime

url = "http://data.taipei/youbike"
#print "downloading with urllib"
data = requests.get(url).json()

conn = pymysql.connect(charset='utf8', host="localhost", user="root", passwd="admin", db="bike")
c = conn.cursor()

for key, value in data["retVal"].items():
    sno = value["sno"]
    tot = value["tot"]
    sbi = value["sbi"]
    bemp = value["bemp"]
    act = value["act"]

sql = "INSERT INTO data(sno,tot,sbi,bemp,act,utime) VALUES(%s,%s,%s,%s,%s,%s)"

print(sno)
c.execute(sql,(sno,tot,sbi,bemp,act,datetime.now()))
conn.commit()


#因為只記錄一天的資料，所以將大於一天的資料清掉
# sql = "DELETE FROM data WHERE TO_DAYS(NOW()) – TO_DAYS(utime) &gt; 1"
# c.execute(sql)
# conn.commit()

conn.close()



# conn = None
# try:
#     conn = pymysql.connect(charset='utf8', host="localhost", user="root", passwd="admin", db="bike")
#     cursor = conn.cursor()
#
#     cursor.execute("SELECT * FROM info ORDER BY sno")
#     # posts = c.fetchall()
#
#     posts = []
#     for obj in cursor.fetchall():
#         posts.append({"sno": obj[0], "sna": obj[1], "sarea": obj[2], "lat": obj[3], "lng": obj[4], "ar": obj[5], "sareaen": obj[6], "snaen": obj[7], "aren": obj[8]})
#     context = {'all_posts': cursor.fetchall()}
#     conn.close()
#
#     print(posts[0]['sna'])
# except pymysql.Error as e:
#     print("Error %d: %s" % (e.args[0], e.args[1]))
#     if conn is not None:
#         conn.close()