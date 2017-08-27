import requests
import lxml.html as ht

class xkcd_grab:
    def __init__(self):
        self.name="xkcd_grab"
        self.rurl="https://c.xkcd.com/random/comic/"

    def request_page(self,url):
         page=requests.get(url)
         parsed=ht.document_fromstring(page.content)
         return parsed

    def get_img_url(self,parsed):
        return 'https://'+parsed.xpath('string(//*[@id="comic"]/img/@src)')[2:]

    def get_random(self):
        return self.get_img_url(self.request_page(self.rurl))
