#coding=gbk
import urllib
import urllib2
import threading
import time 
from collections import deque

proxyQueue = deque()
lock = threading.Lock()

class Proxy:
    def __init__(self,url):
        self.url = url
        self.cnt = 0

class ProxyQueueReader:
    global proxyQueue
    def readFromFile(self):
        fp = open('proxyList','r')
        line = fp.readline()
        while(line):
            proxy = Proxy(line.strip())
            proxyQueue.append(proxy)
            line = fp.readline()
        #print proxyQueue

class QQMusic(threading.Thread):
    proxy = None

    def __init__(self,proxy,no):
        threading.Thread.__init__(self) 
        self.proxy = proxy
        self.no = no
        print 'ThreadId:',no

    def run(self):
        try:
            url='http://y.qq.com/index.html#type=song&mid=000jLqdM0HKQGq'
            proxy_url = 'http://'+self.proxy.url
            proxy_support = urllib2.ProxyHandler({'http': proxy_url})
            opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
            req=urllib2.Request(url)
            req.add_header("Accept-Language","zh-cn") 
            req.add_header("Content-Type","text/html; charset=gb2312")
            req.add_header("User-Agent","Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; .NET CLR 1.1.4322)")
            print 'Try to fetch URL:',url,'User-Agent:',proxy_url
            res=opener.open(req,timeout=10)
            data = res.read()
            #print data
            print "SUCCESS!!!"
        except:
            print 'Fetch fail URL:',url,'User-Agent:',proxy_url 

class ProxyUtils:
    global proxyQueue
    global lock

    def __verifyProxy__(self,proxy):
        proxy_handler = urllib2.ProxyHandler({"http" : proxy.url})
        print 'Start to verify proxy:',proxy.url
        try:
            url='http://y.qq.com/index.html#type=index'
            proxy_url = 'http://'+proxy.url
            proxy_support = urllib2.ProxyHandler({'http': proxy_url})
            opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
            req=urllib2.Request(url)
            req.add_header("Accept-Language","zh-cn") 
            req.add_header("Content-Type","text/html; charset=gb2312")
            req.add_header("User-Agent","Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; .NET CLR 1.1.4322)")
            res=opener.open(req,timeout=3)
            data = res.read()
            if len(data)>1000:
                print 'Verify proxy success',proxy.url
                return True
            else:
                print 'Verify proxy fail',proxy.url
                return False

        except:
            print 'Verify proxy fail',proxy.url
            return False


    def getAvailbleProxy(self):
        while(True):
            if len(proxyQueue)<1:
                print 'The proxyList is Over!!!!'
                return None
            lock.acquire()
            proxy = proxyQueue.popleft()
            lock.release()
            if proxy.cnt >= 4:
                print 'Remove proxy:',proxy.url
                continue
            if self.__verifyProxy__(proxy):
                proxy.cnt = 0
                proxyQueue.append(proxy)
                return proxy
            else:
                proxy.cnt += 1     


if __name__ == '__main__':
    proxyQueueReader = ProxyQueueReader()
    proxyQueueReader.readFromFile()
    proxyUtils = ProxyUtils()
    while(True):
        i=0
        while(True):
            proxy = proxyUtils.getAvailbleProxy()
            qqMusic = QQMusic(proxy,i)
            qqMusic.setDaemon(True)
            qqMusic.start()
            i+=1
        #time.sleep(5)



    

