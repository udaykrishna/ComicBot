import requests
import lxml.html as ht
import datetime as dt
import random
from comic import comic
from json import loads

#week_map={'sunday':0,'monday':1,'tuesday':2,'wednesday':3,'thursday':4,'friday':5,'saturday':6}
class xkcd_grab:
    """
    Base template if random gives another page as response
    """
    def __init__(self):
        self.name="xkcd_grab"
        self.rurl="https://c.xkcd.com/random/comic/"
        self.details=comic('XKCD','Randall Munroe','https://xkcd.com/')

    def get_details(self):
        return str(self.details)

    def request_page(self,url):
         page=requests.get(url)
         parsed=ht.document_fromstring(page.content)
         return parsed

    def get_img_url(self,parsed):
        return 'https://'+parsed.xpath('string(//*[@id="comic"]/img/@src)')[2:]

    def get_random(self):
        return self.get_img_url(self.request_page(self.rurl))

class explosm_grab(xkcd_grab):
    def __init__(self):
        self.name="explosm_grab"
        self.rurl='http://explosm.net/comics/random'
        self.details=comic('cyanide and happiness',['Dave McElfatrick', 'Kris Wilson',
                            'Rob DenBleyker'],'http://explosm.net/')

    def get_img_url(self,parsed):
        return 'http://'+parsed.xpath('string(//*[@id="main-comic"]/@src)')[2:]

class penny_arcade_grab(xkcd_grab):
    """
    Base template if no default random is implemented
    """
    def __init__(self):
        self.name="penny_arcade_grab"
        self.burl='https://www.penny-arcade.com/comic/'
        self.details=comic('Penny Arcade',['Jerry Holkins', 'Mike Krahulik'],'https://www.penny-arcade.com/')

    def gen_rand_rel_date(self,dow=[]):
        today=dt.datetime.today()
        dayoweek=int(dt.datetime.strftime(today,'%w'))
        goto=random.choice(dow)
        backby=int(52*random.random())*7+(dayoweek-goto)
        date=today-dt.timedelta(days=backby)
        return dt.datetime.strftime(date,'%Y/%m/%d/')

    def get_img_url(self,parsed):
        return parsed.xpath('string(//*[@id="comicFrame"]/a/img/@src)')

    def get_random(self):
        return self.get_img_url(self.request_page(self.burl+self.gen_rand_rel_date(dow=[1,3,5])))

class nedroid_grab(xkcd_grab):
    def __init__(self):
        self.name="nedroid_grab"
        self.rurl="http://nedroid.com/?randomcomic=1"
        self.details=comic('Nedroid','Anthony Clark','http://nedroid.com')

    def get_img_url(self,parsed):
        return parsed.xpath('string(//*[@id="comic"]/img/@src)')

class moonbeard_grab(xkcd_grab):
    def __init__(self):
        self.name="moonbeard_grab"
        self.rurl="http://moonbeard.com/?randomcomic"
        self.details=comic('Moonbeard','James Squires','http://moonbeard.com/')

    def get_img_url(self,parsed):
        return parsed.xpath('string(//*[@id="comic-1"]/a/img/@src)')

class smbc_grab(xkcd_grab):
    def __init__(self):
        self.name="smbc_grab"
        self.rurl="http://www.smbc-comics.com/random.php"
        self.details=comic('Saturday Morning Breakfast Cereal','Zach Weiner','http://www.smbc-comics.com/')

    def get_img_url(self,parsed):
        return "http://www.smbc-comics.com"+parsed.xpath('string(//*[@id="cc-comic"]/@src)')

class wumo_grab(penny_arcade_grab):
    def __init__(self):
        self.name="wumo_grab"
        self.burl="http://wumo.com/wumo/"
        self.details=comic('Wumo',['Mikael Wulff', 'Anders Morgenthaler'],'http://wumo.com/')
    def get_img_url(self,parsed):
        return 'http://wumo.com'+parsed.xpath('string(//*[@id="main"]/article[1]/div/a/img/@src)')

    def get_random(self):
        return self.get_img_url(self.request_page(self.burl+self.gen_rand_rel_date(dow=[0,1,2,3,4,5,6])))

class loading_artist_grab(xkcd_grab):
    def __init__(self):
        self.name="loading_artist_grab"
        self.rurl="https://loadingartist.com/random"
        self.details=comic('Loading Artist','Gregor Czaykowski','https://loadingartist.com/')

    def get_img_url(self,parsed):
        return parsed.xpath('string(//div[@class="comic"]/a/img/@src)')

class cad_grab(xkcd_grab):
    """
    Base template if random url response is in json
    """
    def __init__(self):
        self.name="cad_grab"
        self.rurl="https://cad-comic.com/wp-admin/admin-ajax.php?action=get_nav_post&nav_type=random"
        self.details=comic('Ctrl+Alt+Del','Tim Buckley','https://cad-comic.com/')

    def request_page(self,url):
         page=requests.get(url)
         return page

    def get_img_url(self,parsed):
        return str(loads(parsed.content.decode())['comic'])

class adamathome_grab(xkcd_grab):
    """
    Base template for all gocomics
    """
    def __init__(self):
        self.name="adamathome_grab"
        self.rurl="http://www.gocomics.com/random/adamathome"
        self.details=comic('Adam@Home',['Brian Basset (creater)','Rob Harrell (current artist)'],'http://www.gocomics.com/adamathome')

    def get_img_url(self,parsed):
        return parsed.xpath('string(//*[@id="js-item-start"]/div/div[1]/div[1]/a/picture/img/@src)')
