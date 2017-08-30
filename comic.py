class comic:
    def __init__(self,name,author,url):
        self.name=name
        self.url=url
        self.author=author

    def __repr__(self):
        return "Strip is from Comic "+self.name+", by "+self.author+" and is hosted at "+self.url
