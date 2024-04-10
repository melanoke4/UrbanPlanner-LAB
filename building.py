import datetime

class Building:
    def __init__(self,address,stories):
        self.designer = "Mel"
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories
        
    def construct(self):
        self.date_constructed = datetime.datetime.now()
        
    def purchase(self,name):
        self.owner = name
        