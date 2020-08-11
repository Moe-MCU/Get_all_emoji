# -*- coding: UTF-8 -*-
import requests,re
import os
import csv
def get_li(all):
    global l
    herf1 = re.search('<a href="', all, flags=0).span()#切上面
    herf1 = herf1[1]
    href = all[herf1:]
    herf2 = re.search('">', href, flags=0).span()#切下面
    herf2 = herf2[0]
    href = href[:herf2]
    print(href)
    l.append(href)#塞进链表
    del1 = re.search('</li>', all, flags=0).span()#切掉刚塞完的部分
    del1 = del1[1]
    all = all[del1:]
    return all
link="https://emojipedia.org/twitter/" #貌似目前Twitter的Emoji包含了完整的Emoji13.1
html_file=requests.get(link)
html_all=html_file.text
all1 = re.search('<ul class="emoji-grid">', html_all, flags=0).span()#切上面
all1 = all1[1]
all = html_all[all1:]
all2 = re.search('</ul>', all, flags=0).span()#切下面
all2 = all2[0]
all = all[:all2]
li_num=all.count("</li>")#emoji总数计算
print(li_num)
loop_count=0
l=[]
while loop_count < li_num:
    all = get_li(all)#获取每个Emoji对于"https://emojipedia.org/twitter/"的相对路径
    loop_count+=1
with open('out.csv','wt') as f:
    cw = csv.writer(f)
    for item in l:
        cw.writerow([item])#不加[]就成华夫饼🧇
print(loop_count)
