# coding:utf8
import html_downloader
import html_outputer
import html_parser
import url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader=html_downloader.HtmlDownloader()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlParser()
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url) #　把根url加入
        while self.urls.has_new_url(): #　如果新的url
            try:
                new_url = self.urls.get_new_url() # 获得这个url
                print 'craw %d : %s'%(count,new_url)
                html_cont=self.downloader.download(new_url) # 从这个url下载内容
                new_urls, new_data=self.parser.parse(new_url,html_cont) # 从内容中获取url和data
                self.urls.add_new_urls(new_urls) # 将获取的url加到url列表里
                self.outputer.collect_data(new_data) # 输出data

                if count == 10:
                    break
                count = count + 1
            except:
                print "craw failed"
        self.outputer.output_html()
if __name__=="__main__":
    root_url="http://baike.baidu.com/item/SPARK"
    obj_spider= SpiderMain()
    obj_spider.craw(root_url)