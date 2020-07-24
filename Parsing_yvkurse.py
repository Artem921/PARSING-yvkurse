from urllib.request import urlopen
from bs4 import BeautifulSoup  as bs
import numpy as np
import re 
class Parsing(object):
    def __init__(self,url):
        self.url=url
        self.titles=[]
        self.hrefs=[]
        self.text=[]
        self.images=[]
    
    def bs_4(self,url):
        url=urlopen(url)
        return bs(url)
        
        
        
    def parse_title(self):
        span=self.bs_4(self.url).findAll("span",{"class":"author-page-article__title"})
        for title in span:
            self.titles.append(title.get_text()[:])
        self.titles=np.array(self.titles)
        return self.titles
    
    def parse_text(self):
        hrefs=self.bs_4(self.url).findAll("a",href=True)
        for href in hrefs:
            if re.search(r'/@yvkurse-',href['href']):
                href['href']=href['href'].replace('/@yvkurse-','-')
                self.hrefs.append(self.url+href['href'])
        for text_url in self.hrefs:
            parse_text=self.bs_4(text_url)
            parse_text=parse_text.findAll("p",{'class':"article_decoration_first article_decoration_last article_decoration_before"},
                                          recursive=True)
            self.text.append([x.get_text() for x in parse_text])
        self.text=np.array(self.text)
        return self.text
    
    def parse_images(self):
        if self.hrefs==[]:
            print("ValueError:","before calling parse_images(), call parse_text()")
        for images_url in self.hrefs:
            
            parse_image=self.bs_4(images_url)
            parse_image=parse_image.findAll("img",{'class':"article_object_photo__image_blur article_carousel_img"},
                                          recursive=True)
           
            self.images.append([x['src'] for x in parse_image])
        self.images=np.array(self.images)
        return self.images
            
            
