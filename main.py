from building import Building
from city import City
import datetime

fourth_street_condo = Building("4th street", 12)
fourth_street_condo.purchase("Sophie Hatter")
fourth_street_condo.construct()

third_street_condo = Building("3rd street", 111)
third_street_condo.purchase("Howl")
third_street_condo.construct()

second_street_condo = Building("2nd street", 44)
second_street_condo.purchase("Howl")
second_street_condo.construct()

first_street_condo = Building("1st street", 2)
first_street_condo.purchase("Howl")
first_street_condo.construct()

colmar = City("Colmar")
colmar.add_building(fourth_street_condo)
colmar.add_building(third_street_condo)
colmar.add_building(second_street_condo)
colmar.add_building(first_street_condo)
# colmar.buildings.append(fourth_street_condo)

for building in colmar.buildings:
    print(building.address)
    print(building.owner)
    print(building.stories)
