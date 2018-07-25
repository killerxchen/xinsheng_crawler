# 华为心声社区的第一页帖子名称
import requestDetail
import urllib.request
from bs4 import BeautifulSoup

from requestDetail import requestDetailBlog

MAX_PAGE_NUM = 3
i = 0
bbsLinkList = []
bbsTitleList = []
saveDir = "xinshengBlogContent/"
for pageIndex in range(1, MAX_PAGE_NUM, 1):
    # 通过urllib获取页面数据
    url = "http://xinsheng.huawei.com/cn/index.php?app=forum&mod=List&act=index&class=461&p=" + str(pageIndex)
    page = urllib.request.urlopen(url)
    html = page.read()
    # 创建beautifulsoup对象，用来解析页面数据
    soup = BeautifulSoup(html, "html.parser")
    soup.prettify()
    # 根据页面结构，具体解析过程
    bbsDiv = soup.find(attrs={"class": "bbs_list"})
    bbsDiv.stripped_strings
    bbsBlock = bbsDiv.contents[3]  # 空白行也被当做节点 ，每个节点前有个"\n" ，因此，取第二个儿子需要用[4]

    # 具体解析
    bbsUL = bbsBlock.children


    for child in bbsUL:
        if child.name == "li":
            className = child.get('class')
            if className is not None:
                continue
            if '惯例' in child.a.string:
                print("%d:%s" % (i, child.a.string))
                bbsLinkList.append(child.a['href'])
                bbsTitleList.append(child.a.string)
            i += 1

for j in range(len(bbsLinkList)):
    fileObject = open(saveDir +bbsTitleList[j] + ".txt", 'w' ,encoding='UTF-8')#文件编码选utf8，默认是gbk
    detail = requestDetailBlog(bbsLinkList[j])
    if detail is None:
        detail = ""
        continue
    #print (detail)
    fileObject.write(detail)
    fileObject.write('\n')
    fileObject.close()
