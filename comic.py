class comic:
    def __init__(self,name,author,url):
        self.name=name
        self.url=url
        self.author=author

    def __repr__(self):
        return str("A Strip from Comic "+self.name+", by "+str(self.author)+"\n"+self.url)
