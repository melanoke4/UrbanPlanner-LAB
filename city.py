class City():
    def __init__(self,name,year=2024):
        self.name = name
        self.mayor = ""
        self.year_established = year
        self.buildings = list()
        
    def add_building(self,building):
        self.buildings.append(building)
