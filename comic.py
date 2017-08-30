class comic:
    def __init__(self,name,author,url):
        self.name=name
        self.url=url
        self.author=author

    def __repr__(self):
        if type(self.author) is list:
            self.author_str= ','.join(self.author[:-1])+' and '+self.author[-1]
        else:
            self.author_str=str(self.author)
        return str("A Strip from Comic "+self.name+" by "+self.author_str+"\n"+self.url)
