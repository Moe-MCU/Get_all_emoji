# -*- coding: UTF-8 -*-
import requests,re
import os
import csv
url_head="https://emojipedia.org"
filename="out.csv"
l=[[] for i in range(6)]#6栏，相对路径+页面绝对路径+appleEmoji+whatsapp+twitter+facebook
with open(filename,'rt') as f:
   cr = csv.reader(f)
   for row in cr:
       print(row)
       l[0].append(row)#从csv读入相对路径
for i in range(len(l[0])):
    l[1].append(url_head + str(l[0][i])[2:-2])#切掉两边的['']并拼合绝对路径塞进链表
    #print ("序号：%s   name %s 值：%s" % (i+1, l[0][i], l[1][i]))
for i in range(len(l[1])):
    html_file=requests.get(l[1][i])
    html_all=html_file.text
    all1 = re.search('<section class="vendor-list">', html_all, flags=0).span()#切上边
    all1 = all1[1]
    all = html_all[all1:]
    all2 = re.search('</section>', all, flags=0).span()#切下边
    all2 = all2[0]
    all = all[:all2]
    '''
    all1 = re.search('<ul>', all, flags=0).span()
    all1 = all1[1]
    all = all[all1:]
    all2 = re.search('</ul>', all, flags=0).span()#这个</ul>害死人
    all2 = all2[0]
    all = all[:all2]
    '''
    try:
        apple1 = re.search('<a href="/apple/">', all, flags=0).span()
        apple1 = apple1[1]
        apple = all[apple1:]
        apple2 = re.search('"120">', apple, flags=0).span()
        apple2 = apple2[0]
        apple = apple[:apple2]

        apple1 = re.search('<img src="', apple, flags=0).span()
        apple1 = apple1[1]
        apple = apple[apple1:]
        apple2 = re.search('"', apple, flags=0).span()
        apple2 = apple2[0]
        apple = apple[:apple2]
        l[2].append(apple)
    except:
        l[2].append("null")#如果该套emoji缺少此emoji就塞null
    try:
        whatsapp1 = re.search('<a href="/whatsapp/">', all, flags=0).span()
        whatsapp1 = whatsapp1[1]
        whatsapp = all[whatsapp1:]
        whatsapp2 = re.search('"120">', whatsapp, flags=0).span()
        whatsapp2 = whatsapp2[0]
        whatsapp = whatsapp[:whatsapp2]
        whatsapp1 = re.search('<img src="', whatsapp, flags=0).span()
        whatsapp1 = whatsapp1[1]
        whatsapp = whatsapp[whatsapp1:]
        whatsapp2 = re.search('"', whatsapp, flags=0).span()
        whatsapp2 = whatsapp2[0]
        whatsapp = whatsapp[:whatsapp2]
        l[3].append(whatsapp)
    except:
        l[3].append("null")#如果该套emoji缺少此emoji就塞null
    try:
        twitter1 = re.search('<a href="/twitter/">', all, flags=0).span()
        twitter1 = twitter1[1]
        twitter = all[twitter1:]
        twitter2 = re.search('"120">', twitter, flags=0).span()
        twitter2 = twitter2[0]
        twitter = twitter[:twitter2]

        twitter1 = re.search('<img src="', twitter, flags=0).span()
        twitter1 = twitter1[1]
        twitter = twitter[twitter1:]
        twitter2 = re.search('"', twitter, flags=0).span()
        twitter2 = twitter2[0]
        twitter = twitter[:twitter2]
        l[4].append(twitter)
    except:
        l[4].append("null")#如果该套emoji缺少此emoji就塞null
    try:
        facebook1 = re.search('<a href="/facebook/">', all, flags=0).span()
        facebook1 = facebook1[1]
        facebook = all[facebook1:]
        facebook2 = re.search('"120">', facebook, flags=0).span()
        facebook2 = facebook2[0]
        facebook = facebook[:facebook2]

        facebook1 = re.search('<img src="', facebook, flags=0).span()
        facebook1 = facebook1[1]
        facebook = facebook[facebook1:]
        facebook2 = re.search('"', facebook, flags=0).span()
        facebook2 = facebook2[0]
        facebook = facebook[:facebook2]
        l[5].append(facebook)
    except:
        l[5].append("null")#如果该套emoji缺少此emoji就塞null
    print ("%s name %s apple %s whatsapp %s twitter %s facebook %s" % (i+1,l[0][i],l[2][i],l[3][i],l[4][i],l[5][i]))
with open('out_url.csv','wt') as fo:
    cw = csv.writer(fo)
    for item in l:
        cw.writerow(item)#塞
