# -*- coding: UTF-8 -*-
import os
import requests
from time import time
#from multiprocessing.pool import ThreadPool
import numpy as np
import urllib
import ssl
#import threading

#import urllib2
ssl._create_default_https_context = ssl._create_unverified_context#urllib HTTPS大坑
def url_response(url):
    name, url, apple, whatsapp, twitter, facebook = url
    path  = name[3:-3]#切掉两边["//"]
    print(apple)
    os.mkdir("emoji/"+path)#创建该emoji独立目录
    if apple != "null":
        urllib.request.urlretrieve(apple, "emoji/"+path+"/"+path+"_a.png")#apple下载
    if whatsapp != "null":
        urllib.request.urlretrieve(whatsapp, "emoji/"+path+"/"+path+"_w.png")#whatsapp下载
    if twitter != "null":
        urllib.request.urlretrieve(twitter, "emoji/"+path+"/"+path+"_t.png")#twitter下载
    if facebook != "null":
        urllib.request.urlretrieve(facebook, "emoji/"+path+"/"+path+"_f.png")#facebook下载
filename="URLS_final.csv"
tmp = np.loadtxt(filename, dtype=np.str, delimiter=",")
data = tmp[0:,0:].astype(np.str)#加载数据部分
count_num=0
num_all=len(data)
start = time()
print(num_all)
for x in data:
    url_response(x)
    #t = threading.Thread(target=url_response,args=x)#多线程待填坑
    #threads.append(t)
    #t.start()
    count_num+=1
    print(count_num/num_all)#等的时候给点盼的233
#ThreadPool(4000).imap_unordered(url_response, data)
print(f"Time to download: {time() - start}")
