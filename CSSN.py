#coding=gbk
import urllib2
import time

cnt=0
while cnt<100:
    try:
        urllib2.urlopen('http://bbs.cssn.cn/forum.php?mod=viewthread&tid=318276')
    except:
        print "OK"
    print cnt
    cnt+=1



    

