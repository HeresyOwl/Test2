#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import pymysql

url = "http://data.taipei/youbike"
data = requests.get(url).json()

conn = pymysql.connect(charset='utf8', host="localhost", user="root", passwd="admin", db="bike")
c = conn.cursor()

for key, value in data["retVal"].items():
    sno = value["sno"]
    sna = value["sna"]
    sarea = value["sarea"]
    lat = value["lat"]
    lng = value["lng"]
    ar = value["ar"]
    sareaen = value["sareaen"]
    snaen = value["snaen"]
    aren = value["aren"]

sql = "INSERT INTO info(sno,sna,sarea,lat,lng,ar,sareaen,snaen,aren) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
try:
    c.execute(sql,(sno,sna,sarea,lat,lng,ar,sareaen,snaen,aren) )
    conn.commit()
except:
    print ("Mysql Error")

conn.close()