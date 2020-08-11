# Get_all_emoji
爬Emoji图像的（
## 0x1 获取相对路径
	emoji_spider.py
    输出out.csv
## 0x2 获取emoji图像url
	get_all_url.py
    这里获取了Apple WhatsApp Twitter Facebook的Emoji
    输出out_url.csv
## 0x3 手动处理一下数据
	用Excle把横纵转一下
### 大坑：Excle存完后会给csv头上加上BOM numpy读取时会出问题
### 这里用UltraEdit删除了头部三子节的BOM
## 0x4 下载全部图像
	download.py
    URLS_final.csv 为处理完后的全部url
    下就完了（多线程待填坑
    每个Emoji存进单独的目录