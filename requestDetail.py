import urllib.request
from bs4 import BeautifulSoup


def requestDetailBlog(url):
    #print(url)
    page = urllib.request.urlopen(url)
    html = page.read()
    soup = BeautifulSoup(html, "html.parser")
    soup.prettify()
    while True:
        bbsBlock = soup.find(attrs={"class": "topic-fontBlock"})
        if bbsBlock is not None:
            #print("branch:1")
            bbsBlock = bbsBlock.get_text(strip=True)#去除前面的空白
            break
        bbsBlock = soup.find(attrs={"class": "info "})
        if bbsBlock is not None:
            #print("branch:2")
            bbsBlock = bbsBlock.get_text(strip=True)#去除前面的空白
            break
        bbsBlock = soup.find(attrs={"class": "bbs_info_right_text "})
        if bbsBlock is not None:
            #print("branch:3")
            bbsBlock = bbsBlock.get_text(strip=True)#去除前面的空白
            break;
        #print("branch:4")
        break
    if bbsBlock is None:
        return None
    #print(bbsBlock)
    return bbsBlock